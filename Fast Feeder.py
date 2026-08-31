#Pygame is used to make games.
    #Use the function that loads and displays images, play audio (maybe include sound effects)
    #Use the timer module to time the game

#Game description:
#Creating a game where the user (represented as a circle) has to eat the food (represented in blocks) within a minute
    #Initial total will be 0
    #Keeps on increasing as the user eats more within a minute
    #If the player beats their best score, a congrats message shows and there will be an extra of 30 more minutes added
        #This involves accumulation

import pygame
import time
import random
import math
import os

pygame.font.init()

# Window Configuration
width, height = 1000, 800
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("FAST EATER: TIME TRIAL")

# Asset Safe-Loading
try:
    BG = pygame.transform.scale(pygame.image.load("BG_image.jpeg"), (width, height))
except:
    BG = pygame.Surface((width, height))
    BG.fill((15, 15, 25)) 

# Game Variables
player_size = 65  # Increased from 40 to 65 for a much larger collision zone!
player_vel = 8  

font_large = pygame.font.SysFont("arial", 40, bold=True)
font_small = pygame.font.SysFont("arial", 28)

SCORE_FILE = "highscore.txt"

def load_best_time():
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE, "r") as f:
                return float(f.read().strip())
        except:
            return 0.00
    return 0.00

def save_best_time(new_best):
    with open(SCORE_FILE, "w") as f:
        f.write(f"{new_best:.2f}")

def format_time_string(total_seconds):
    if total_seconds < 60:
        return f"{total_seconds:.2f}s"
    minutes = int(total_seconds // 60)
    remaining_seconds = total_seconds % 60
    return f"{minutes}m {remaining_seconds:.1f}s"

def draw(player, current_time, best_time, foods, particles, screen_shake, threat_level, stage_name, stage_color):
    render_offset_x = random.randint(-screen_shake, screen_shake) if screen_shake > 0 else 0
    render_offset_y = random.randint(-screen_shake, screen_shake) if screen_shake > 0 else 0
    
    dis.blit(BG, (render_offset_x, render_offset_y)) 

    for p in particles:
        pygame.draw.circle(dis, p["color"], (int(p["x"] + render_offset_x), int(p["y"] + render_offset_y)), int(p["size"]))

    # Draw UI Text HUD
    time_str = format_time_string(current_time)
    best_str = format_time_string(best_time)
    
    time_text = font_large.render(f"TIME: {time_str}", 1, (255, 255, 255))
    best_text = font_small.render(f"BEST: {best_str}", 1, (255, 215, 0)) 
    dis.blit(time_text, (20, 20))
    dis.blit(best_text, (20, 70))

    # Draw Dynamic Difficulty Phase Label
    stage_text = font_small.render(f"PHASE: {stage_name}", 1, stage_color)
    dis.blit(stage_text, (20, 110))

    # Draw Threat Warning Bar
    bar_width = 250
    bar_height = 20
    pygame.draw.rect(dis, (50, 50, 50), (width - bar_width - 20, 20, bar_width, bar_height), border_radius=5)
    fill_width = int(bar_width * (threat_level / 100))
    if fill_width > 0:
        pygame.draw.rect(dis, (255, 30, 30), (width - bar_width - 20, 20, fill_width, bar_height), border_radius=5)
    threat_text = font_small.render("THREAT LEVEL", 1, (255, 100, 100))
    dis.blit(threat_text, (width - bar_width - 20, 45))

    # Draw Food
    for food in foods:
        pygame.draw.rect(dis, food["color"], (food["rect"].x + render_offset_x, food["rect"].y + render_offset_y, food["rect"].width, food["rect"].height), border_radius=4)

    # Draw Player (Bigger bounding footprint visual representation)
    pulse = 3 * math.sin(time.time() * 10)
    pygame.draw.circle(dis, (0, 191, 255), (player.centerx + render_offset_x, player.centery + render_offset_y), (player_size // 2) + int(pulse))
    pygame.draw.circle(dis, (255, 255, 255), (player.centerx + render_offset_x, player.centery + render_offset_y), (player_size // 4), 2) 

    pygame.display.update()                 

def run_game_session():
    best_time = load_best_time()
    player = pygame.Rect(width // 2, height // 2, player_size, player_size)

    clock = pygame.time.Clock()
    start_time = time.time()

    food_spawn_timer = 0
    foods = []
    particles = []
    screen_shake = 0
    threat_level = 0.0 

    pygame.mixer.init()
    try:
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(-1)
    except:
        pass

    while True:
        clock.tick(60)
        current_time = time.time() - start_time
        food_spawn_timer += 1

        if screen_shake > 0:
            screen_shake -= 1

        if threat_level >= 100:
            pygame.mixer.music.stop()
            return current_time, best_time

        # --- Balanced Accessible Difficulty Curve ---
        if current_time < 20:
            stage_name = "EASY"
            stage_color = (76, 175, 80)      
            speed_multiplier = 0.8           
            spawn_delay = 55                 
            spawn_count = 1                  
            miss_penalty = 5.0               
        elif current_time < 50:
            stage_name = "MEDIUM"
            stage_color = (255, 152, 0)     
            speed_multiplier = 1.1           
            spawn_delay = 40                 
            spawn_count = 1                  
            miss_penalty = 8.0
        else:
            stage_name = "HARD"
            stage_color = (244, 67, 54)      
            speed_multiplier = 1.4           
            spawn_delay = 25                 
            spawn_count = 2                  
            miss_penalty = 12.0              

        # Dynamic Spawning 
        if food_spawn_timer > spawn_delay:
            for _ in range(spawn_count):
                f_w = random.randint(15, 25)
                f_h = random.randint(15, 25)
                food_x = random.randint(0, width - f_w)
                food_rect = pygame.Rect(food_x, -f_h, f_w, f_h)
                
                foods.append({
                    "rect": food_rect,
                    "color": stage_color,
                    "speed": random.uniform(2.0, 3.5) * speed_multiplier
                })
            food_spawn_timer = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None, best_time

        # Movement Inputs
        keys = pygame.key.get_pressed()        
        moved = False
        if keys[pygame.K_LEFT] and player.x - player_vel >= 0:       
            player.x -= player_vel     
            moved = True
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.width <= width:
            player.x += player_vel     
            moved = True
        if keys[pygame.K_UP] and player.y - player_vel >= 0:
            player.y -= player_vel
            moved = True
        if keys[pygame.K_DOWN] and player.y + player_vel + player.height <= height:
            player.y += player_vel
            moved = True

        if moved:
            particles.append({
                "x": player.centerx + random.randint(-8, 8),
                "y": player.centery + random.randint(-8, 8),
                "size": random.randint(5, 8),
                "color": (0, 191, 255, 120),
                "life": 12
            })

        for p in particles[:]:
            p["life"] -= 1
            p["size"] -= 0.3
            if p["life"] <= 0 or p["size"] <= 0:
                particles.remove(p)

        # Collision Handling
        for food in foods[:]:
            food["rect"].y += food["speed"]    
            if food["rect"].y > height:
                foods.remove(food)
                threat_level += miss_penalty 
            elif food["rect"].colliderect(player):
                foods.remove(food)
                screen_shake = 4 
                threat_level = max(0.0, threat_level - 12.0) 
                
                for _ in range(12):
                    particles.append({
                        "x": player.centerx,
                        "y": player.centery,
                        "size": random.randint(4, 9),
                        "color": food["color"],
                        "life": 18
                    })

        draw(player, current_time, best_time, foods, particles, screen_shake, threat_level, stage_name, stage_color)

def main():
    game_active = True
    
    while game_active:
        final_time, initial_best = run_game_session()
        if final_time is None:
            break
            
        show_summary = True
        is_new_record = final_time > initial_best
        if is_new_record:
            save_best_time(final_time)

        while show_summary:
            dis.fill((10, 10, 15))
            final_time_str = format_time_string(final_time)
            record_time_str = format_time_string(max(final_time, initial_best))

            if is_new_record:
                msg_line1 = "NEW RECORD SMASHED!"
                msg_line2 = f"Survival Time: {final_time_str}"
                color = (255, 215, 0)
            else:
                msg_line1 = "GAME OVER"
                msg_line2 = f"Survived: {final_time_str} | Best: {record_time_str}"
                color = (255, 70, 70)

            text1 = font_large.render(msg_line1, 1, color)
            text2 = font_small.render(msg_line2, 1, (255, 255, 255))
            prompt_text = font_small.render("Press SPACEBAR to Play Again or ESC to Quit", 1, (150, 150, 150))
            
            dis.blit(text1, (width/2 - text1.get_width()/2, height/2 - 80))
            dis.blit(text2, (width/2 - text2.get_width()/2, height/2 - 10))
            dis.blit(prompt_text, (width/2 - prompt_text.get_width()/2, height/2 + 70))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    show_summary = False
                    game_active = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        show_summary = False 
                    if event.key == pygame.K_ESCAPE:
                        show_summary = False
                        game_active = False

    pygame.quit()

if __name__ == "__main__":       
    main()


