#!/usr/bin/env python3
from asyncio import sleep
from colorama import Fore, Style
import cv2
import json
import argparse
import numpy as np
from datetime import datetime


# Inicializa a captura de vídeo da câmera
cap = cv2.VideoCapture(0)

def main():
    parser = argparse.ArgumentParser(description='Definition of test mode')
    parser.add_argument('-j', '--json', type=str, required=True, help='Full path to json file.')
    args = parser.parse_args()
    print(args)
    # Carregua os limites de cor a partir do arquivo JSON
    with open(args.json, 'r') as file:
        limits=json.load(file)

    # Define a tela em branco
    screen = np.full((480, 640, 3),255, dtype=np.uint8)

    # Define as variáveis iniciais para a cor e tamanho do lápis
    pencil_color = (0, 0, 255)  # Vermelho inicialmente
    pencil_size = 2 
    


    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Converta a imagem para o espaço de cores HSV (recomendado para detecção de cor)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Aplique a detecção de cor com base nos limites lidos do arquivo JSON
        mask = cv2.inRange(hsv, (limits['limits']['B']['min'], limits['limits']['G']['min'], limits['limits']['R']['min']),
                       (limits['limits']['B']['max'], limits['limits']['G']['max'], limits['limits']['R']['max']))

        # Encontre os contornos do objeto de maior área na máscara
        

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)

            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                # Desenhe o centróide com uma cruz vermelha na imagem original
                cv2.drawMarker(frame, (cX, cY), (0, 0, 255), markerType=cv2.MARKER_CROSS, markerSize=10, thickness=2)

                # Use o centróide para desenhar na tela
                if pencil_size % 2 == 0:
                    cv2.circle(frame, (cX, cY), pencil_size // 2, pencil_color, -1)
                    cv2.circle(screen, (cX, cY), pencil_size // 2, pencil_color, -1)
                else: 
                    cv2.circle(frame, (cX, cY), pencil_size // 2, pencil_color, -1)
                    cv2.circle(screen, (cX, cY), pencil_size // 2, pencil_color, -1)
        



        ############## A2 ############


        # Mostrar a imagem original
        frame_sized=cv2.resize(frame,(600,400))
        key = cv2.waitKey(1)
        new_background=screen

        if key == ord('s'):
            # Redimensione o novo fundo para o tamanho da imagem original
           
            new_background = cv2.resize(frame, (screen.shape[1], screen.shape[0]))
            print("\n" + Fore.YELLOW + 'New frame'+ Style.RESET_ALL)
            
        elif key == ord('n'):
            canvas = np.full((480, 640, 3),255, dtype=np.uint8)

            new_background = cv2.resize(canvas, (screen.shape[1], screen.shape[0]))
            print("\n" + Fore.YELLOW + 'New canvas'+ Style.RESET_ALL)

        gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        _, mask2 = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        # Inverta a máscara
        mask_inverted = cv2.bitwise_not(mask2)

        # Extraia o objeto (desenho) da imagem original
        object = cv2.bitwise_and(screen, screen, mask=mask_inverted)

        # Combine o objeto com o novo fundo
        screen = cv2.bitwise_and(new_background, new_background, mask=mask2) + object


        ############## Visualizaçao ############



        cv2.imshow('Original Image', cv2.flip(frame_sized,1))

        # Mostrar a tela em branco
    
        cv2.imshow('Drawing', cv2.flip(screen,1))

        #key = cv2.waitKey(1) 
        if key == ord('r'):
             pencil_color = (0, 0, 255)  # Vermelho
             print('Selected color to ' + Fore.RED + 'red' + Style.RESET_ALL)

        elif key == ord('g'):
            pencil_color = (0, 255, 0)  # Verde
            print('Selected color to ' + Fore.GREEN + 'green' + Style.RESET_ALL)

        elif key == ord('b'):
            pencil_color = (255, 0, 0)  # Azul
            print('Selected color to '+ Fore.BLUE +  'blue' + Style.RESET_ALL)

        elif key == ord('+'):
            pencil_size += 2
            print('Pencil size increased to: '+ Fore.YELLOW + str(pencil_size)+ Style.RESET_ALL)

        elif key == ord('-'):
            pencil_size = max(1, pencil_size - 2)
            print('Pencil size decreased to: '+ Fore.YELLOW + str(pencil_size)+ Style.RESET_ALL)

        elif key == ord('c'):
            screen = np.full((480, 640, 3),255, dtype=np.uint8)
            print("\n" + Fore.YELLOW + 'New canvas'+ Style.RESET_ALL)

        elif key == ord('w'):
        # Gere um nome de arquivo com base na data e hora atual
            current_time = datetime.now().strftime("%a_%b_%d_%H:%M:%S_%Y")
            filename = f'drawing_{current_time}.png'
            cv2.imwrite(filename, screen)
            print("\n" + Fore.YELLOW + 'Saved canvas'+ Style.RESET_ALL)

        elif key == ord('q'):
            print ("\n" + Fore.RED + 'Program interrupted'+ Style.RESET_ALL)
            break

if __name__ == '__main__':
    main()
