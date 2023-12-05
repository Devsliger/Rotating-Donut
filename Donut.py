import pygame
import math

pygame.init()


theta_spacing = 0.07
phi_spacing = 0.02
screen_width = 800
screen_height = 600
R1 = 1
R2 = 2
K2 = 5
K1 = screen_width * K2 * 3 / (8 * (R1 + R2))


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rotating Donut")


def render_frame(A, B):

    cosA, sinA = math.cos(A), math.sin(A)
    cosB, sinB = math.cos(B), math.sin(B)


    output = [[' ' for _ in range(screen_width)] for _ in range(screen_height)]
    zbuffer = [[0 for _ in range(screen_width)] for _ in range(screen_height)]


    for theta in range(int(2 * math.pi / theta_spacing)):
        costheta, sintheta = math.cos(theta * theta_spacing), math.sin(theta * theta_spacing)


        for phi in range(int(2 * math.pi / phi_spacing)):
            cosphi, sinphi = math.cos(phi * phi_spacing), math.sin(phi * phi_spacing)


            circlex = R2 + R1 * costheta
            circley = R1 * sintheta


            x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
            y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
            z = K2 + cosA * circlex * sinphi + circley * sinA
            ooz = 1 / z


            xp = int(screen_width / 2 + K1 * ooz * x)
            yp = int(screen_height / 2 - K1 * ooz * y)


            if 0 <= xp < screen_width and 0 <= yp < screen_height:

                L = cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta + cosB * (
                        cosA * sintheta - costheta * sinA * sinphi)


                if L > 0:

                    if ooz > zbuffer[yp][xp]:
                        zbuffer[yp][xp] = ooz
                        luminance_index = int(L * 8)
                        output[yp][xp] = ".,-~:;=!*#$@"[luminance_index]


    for y in range(screen_height):
        for x in range(screen_width):
            color = pygame.Color(255, 255, 255) if output[y][x] == ' ' else pygame.Color(0, 0, 0)
            screen.set_at((x, y), color)


    pygame.display.flip()


clock = pygame.time.Clock()
frame_count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame_count += 1
    A = frame_count * 0.04
    B = frame_count * 0.02
    render_frame(A, B)


    clock.tick(30)


pygame.quit()
