import pygame, os
from pygame.locals import *
from math import sin, cos, pi

pygame.init()
screen = pygame.display.set_mode((0, 0), FULLSCREEN)
font = pygame.font.SysFont('impact', 50)
running = True

smoke_particles = list()


def generate_smoke(direction: int, velocity: float, color: tuple[int, int, int], xy: tuple[float, float]):
    global smoke_particles
    smoke_particles.append({'direction': direction, 'velocity': velocity, 'color': color, 'x': xy[0], 'y': xy[1], 'size': 5})


def render_smoke():
    global smoke_particles
    while True:
        try:
            for num, particle in enumerate(smoke_particles):
                pygame.draw.rect(screen, particle['color'], (particle['x'] - particle['size'] / 2, particle['y'] - particle['size'] / 2, particle['size'], particle['size']))
                particle['velocity'] -= 0.1 if velocity > 0 else 0
                particle['size'] += 1
                particle['x'] += particle['velocity'] * cos(particle['direction'] * (pi / 180))
                particle['y'] -= particle['velocity'] * sin(particle['direction'] * (pi / 180))
                smoke_particles[num] = particle
                if particle['size'] == 40:
                    smoke_particles.pop(num)
            break
        except:
            pass


velocity = 0
change_velocity = 1

xr = screen.get_rect()[2] // 2 - 20
yr = screen.get_rect()[3] // 2
rr = 270

xg = screen.get_rect()[2] // 2
yg = screen.get_rect()[3] // 2 - 20
rg = 180

xb = screen.get_rect()[2] // 2 + 20
yb = screen.get_rect()[3] // 2
rb = 90

xw = screen.get_rect()[2] // 2
yw = screen.get_rect()[3] // 2 + 20
rw = 0


while running:
    pygame.time.Clock().tick(60)
    screen.fill((0, 0, 0))

    generate_smoke(rr - 90, 9, (255, 0, 0), (xr, yr))
    generate_smoke(rg - 90, 9, (0, 255, 0), (xg, yg))
    generate_smoke(rb - 90, 9, (0, 0, 255), (xb, yb))
    generate_smoke(rw - 90, 9, (255, 255, 255), (xw, yw))

    render_smoke()

    pygame.draw.circle(screen, (255, 0, 0), (xr, yr), 10)
    pygame.draw.circle(screen, (0, 255, 0), (xg, yg), 10)
    pygame.draw.circle(screen, (0, 0, 255), (xb, yb), 10)
    pygame.draw.circle(screen, (255, 255, 255), (xw, yw), 10)
    pygame.draw.circle(screen, (255, 255, 0), (screen.get_rect()[2] // 2, screen.get_rect()[3] // 2), 20)


    xr += velocity * cos(rr * (pi / 180))
    yr -= velocity * sin(rr * (pi / 180))
    rr += 1.4 * (velocity / 0.5)

    xg += velocity * cos(rg * (pi / 180))
    yg -= velocity * sin(rg * (pi / 180))
    rg += 1.4 * (velocity / 0.5)

    xb += velocity * cos(rb * (pi / 180))
    yb -= velocity * sin(rb * (pi / 180))
    rb += 1.4 * (velocity / 0.5)

    xw += velocity * cos(rw * (pi / 180))
    yw -= velocity * sin(rw * (pi / 180))
    rw += 1.4 * (velocity / 0.5)


    if velocity < -100:
        change_velocity = 1
    elif velocity > 100:
        change_velocity = -1

    velocity += 0.01 * change_velocity


    txt = 'Velocity: {:.2f}'.format(velocity)
    txt = font.render(txt, True, (255, 100, 155))
    txt_pos = txt.get_rect(topright=(screen.get_rect()[2], 0))
    screen.blit(txt, txt_pos)
    
    pygame.display.flip()

    for ev in pygame.event.get():
        if ev.type == KEYDOWN:
            if ev.key == K_END:
                running = False
        elif ev.type == QUIT:
            running = False

    pygame.mouse.set_visible(False)

pygame.quit()
