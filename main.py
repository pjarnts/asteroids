import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for asteroid in asteroids:
            if asteroid.collision(player):
                exit("Game over!")
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid1, asteroid2 = asteroid.split()
                    if asteroid1 is not None and asteroid2 is not None:
                        asteroids.add(asteroid1)
                        asteroids.add(asteroid2)

        updatable.update(dt)


        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        remaining_time = clock.tick(60)
        dt = remaining_time / 1000
if __name__ == "__main__":
    main()

