import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    Player.containers = (updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def reset_game():
        player.position.update(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        player.velocity.update(0, 0)
        player.rotation = 0
        asteroid_group.empty()
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    # print("TURN:", PLAYER_TURN_SPEED)
    while True:
        screen.fill("black")
        # player.draw(screen)
        
        updatable_group.update(dt)
        for asteroid in asteroid_group:
            if asteroid.radius < 30:  # or whatever "small" is
                d = player.position.distance_to(asteroid.position)
                print("small r:", asteroid.radius, "dist:", d, "sum:", player.radius + asteroid.radius)
            if player.collision(asteroid):
                print("Game over!")
                pygame.time.delay(600)
                reset_game()
                break
            for shot in shots_group:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()


        for sprite in drawable_group:
            sprite.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60)/1000
        pygame.display.flip()

         
if __name__ == "__main__":
    main()
