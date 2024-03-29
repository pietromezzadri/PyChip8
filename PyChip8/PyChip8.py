from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame, Render, Input, Chip8

chip8_fontset = [
  0xF0, 0x90, 0x90, 0x90, 0xF0, # 0
  0x20, 0x60, 0x20, 0x20, 0x70, # 1
  0xF0, 0x10, 0xF0, 0x80, 0xF0, # 2
  0xF0, 0x10, 0xF0, 0x10, 0xF0, # 3
  0x90, 0x90, 0xF0, 0x10, 0x10, # 4
  0xF0, 0x80, 0xF0, 0x10, 0xF0, # 5
  0xF0, 0x80, 0xF0, 0x90, 0xF0, # 6
  0xF0, 0x10, 0x20, 0x40, 0x40, # 7
  0xF0, 0x90, 0xF0, 0x90, 0xF0, # 8
  0xF0, 0x90, 0xF0, 0x10, 0xF0, # 9
  0xF0, 0x90, 0xF0, 0x90, 0x90, # A
  0xE0, 0x90, 0xE0, 0x90, 0xE0, # B
  0xF0, 0x80, 0x80, 0x80, 0xF0, # C
  0xE0, 0x90, 0x90, 0x90, 0xE0, # D
  0xF0, 0x80, 0xF0, 0x80, 0xF0, # E
  0xF0, 0x80, 0xF0, 0x80, 0x80  # F
  ]

def main():
    renderer = Render.Renderer(64,32, 10)
    input = Input.Input()
    chip8 = Chip8.chip8(chip8_fontset)
    chip8.load_game("pong.rom")
    running = 1
    clock = pygame.time.Clock()

    renderer.clear_screen()
    
    while running:
        #clock.tick()
        chip8.emulate_cycle(renderer.sound)
        #if chip8.opcode != 0:
        #    print(chip8.opcode)
        if (chip8.draw_flag):
            renderer.draw_graphics(chip8.gfx, (255,255,255))

        running = input.event_handler()
        if input.key_down:
            chip8.key[input.key_pressed] = 1
        else:
            chip8.key[input.key_pressed] = 0


main()