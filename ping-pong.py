import pygame
import random

# Configurações do jogo
largura_tela = 640
altura_tela = 480
tamanho_jogador = 50
tamanho_bola = 15
velocidade_jogador = 1
velocidade_bola = 0.1

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

def desenhar_retangulo(tela, cor, pos_x, pos_y, largura, altura):
    pygame.draw.rect(tela, cor, pygame.Rect(pos_x, pos_y, largura, altura))

def desenhar_pontuacao(tela, fonte, jogador1_pontos, jogador2_pontos):
    texto_jogador1 = fonte.render(f'Jogador 1: {jogador1_pontos}', True, BRANCO)
    texto_jogador2 = fonte.render(f'Jogador 2: {jogador2_pontos}', True, BRANCO)
    tela.blit(texto_jogador1, (20, 20))
    tela.blit(texto_jogador2, (largura_tela - 150, 20))

def main():
    pygame.init()
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption('Mini Jogo de Pong')

    fonte = pygame.font.Font(None, 36)

    jogador1_pos_y = altura_tela // 2 - tamanho_jogador // 2
    jogador2_pos_y = altura_tela // 2 - tamanho_jogador // 2
    bola_pos_x = largura_tela // 2 - tamanho_bola // 2
    bola_pos_y = altura_tela // 2 - tamanho_bola // 2

    velocidade_jogador1 = 0
    velocidade_jogador2 = 0
    velocidade_bola_x = velocidade_bola * random.choice((1, -1))
    velocidade_bola_y = velocidade_bola * random.choice((1, -1))

    jogador1_pontos = 0
    jogador2_pontos = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    velocidade_jogador1 = -velocidade_jogador
                elif event.key == pygame.K_s:
                    velocidade_jogador1 = velocidade_jogador
                elif event.key == pygame.K_UP:
                    velocidade_jogador2 = -velocidade_jogador
                elif event.key == pygame.K_DOWN:
                    velocidade_jogador2 = velocidade_jogador

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    velocidade_jogador1 = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    velocidade_jogador2 = 0

        jogador1_pos_y += velocidade_jogador1
        jogador2_pos_y += velocidade_jogador2

        bola_pos_x += velocidade_bola_x
        bola_pos_y += velocidade_bola_y

        # Restringe o movimento dos jogadores
        jogador1_pos_y = max(jogador1_pos_y, 0)
        jogador1_pos_y = min(jogador1_pos_y, altura_tela - tamanho_jogador)
        jogador2_pos_y = max(jogador2_pos_y, 0)
        jogador2_pos_y = min(jogador2_pos_y, altura_tela - tamanho_jogador)

        # Verifica colisões com as bordas
        if bola_pos_y < 0 or bola_pos_y > altura_tela - tamanho_bola:
            velocidade_bola_y = -velocidade_bola_y

        # Verifica colisões com os jogadores
        if bola_pos_x < tamanho_jogador and jogador1_pos_y < bola_pos_y < jogador1_pos_y + tamanho_jogador:
            velocidade_bola_x = -velocidade_bola_x
        elif bola_pos_x > largura_tela - tamanho_jogador - tamanho_bola and jogador2_pos_y < bola_pos_y < jogador2_pos_y + tamanho_jogador:
            velocidade_bola_x = -velocidade_bola_x

        # Verifica se a bola ultrapassa as bordas laterais
        if bola_pos_x < 0:
            # Ponto para o jogador 2
            jogador2_pontos += 1
            bola_pos_x = largura_tela // 2 - tamanho_bola // 2
            bola_pos_y = altura_tela // 2 - tamanho_bola // 2
            velocidade_bola_x = velocidade_bola * random.choice((1, -1))
            velocidade_bola_y = velocidade_bola * random.choice((1, -1))
        elif bola_pos_x > largura_tela:
            # Ponto para o jogador 1
            jogador1_pontos += 1
            bola_pos_x = largura_tela // 2 - tamanho_bola // 2
            bola_pos_y = altura_tela // 2 - tamanho_bola // 2
            velocidade_bola_x = velocidade_bola * random.choice((1, -1))
            velocidade_bola_y = velocidade_bola * random.choice((1, -1))

        tela.fill(PRETO)
        desenhar_retangulo(tela, BRANCO, 0, jogador1_pos_y, 10, tamanho_jogador)
        desenhar_retangulo(tela, BRANCO, largura_tela - 10, jogador2_pos_y, 10, tamanho_jogador)
        desenhar_retangulo(tela, BRANCO, bola_pos_x, bola_pos_y, tamanho_bola, tamanho_bola)
        desenhar_pontuacao(tela, fonte, jogador1_pontos, jogador2_pontos)

        pygame.display.flip()

if __name__ == "__main__":
    main()
