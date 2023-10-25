#!/usr/bin/env python3
from asyncio import sleep
import pprint
import cv2
import json

# Crie uma função para o callback das trackbars para atualizar os limites de cor
def update_limits(x):
    pass

# Inicialize a captura de vídeo da câmera
cap = cv2.VideoCapture(0)


def main():
    #Crie janelas OpenCV para mostrar a imagem original e a máscara de segmentação
    cv2.namedWindow('Original Image')
    cv2.namedWindow('Color Mask')

    # Crie trackbars para os limites de cor
    cv2.createTrackbar('Bmin', 'Color Mask', 0, 255, update_limits)
    cv2.createTrackbar('Bmax', 'Color Mask', 255, 255, update_limits)
    cv2.createTrackbar('Gmin', 'Color Mask', 0, 255, update_limits)
    cv2.createTrackbar('Gmax', 'Color Mask', 255, 255, update_limits)
    cv2.createTrackbar('Rmin', 'Color Mask', 0, 255, update_limits)
    cv2.createTrackbar('Rmax', 'Color Mask', 255, 255, update_limits)

    prev_minr=0
    prev_ming=0
    prev_minb=0
    prev_maxb=0
    prev_maxg=0
    prev_maxr=0
    i= 0

    while True:
        ret, frame = cap.read()
        

        if not ret:
          break

        # Converte a imagem para o espaço de cores HSV 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Obtenha os valores atuais das trackbars
        min_b = cv2.getTrackbarPos('Bmin', 'Color Mask')
        max_b = cv2.getTrackbarPos('Bmax', 'Color Mask')

        min_g = cv2.getTrackbarPos('Gmin', 'Color Mask')
        max_g = cv2.getTrackbarPos('Gmax', 'Color Mask')

        min_r = cv2.getTrackbarPos('Rmin', 'Color Mask')
        max_r = cv2.getTrackbarPos('Rmax', 'Color Mask')

        color_data = [
                {'color':'Blue', 'min': min_b, 'prev_min': prev_minb},
                {'color':'Red', 'min': min_r, 'prev_min': prev_minr},
                {'color':'Green', 'min': min_g, 'prev_min': prev_ming}]
        
        def getMin(dict):
           i = 1
           min = dict[i]['min']
           return min
        
        def getPrevMin(dict):
           i = 1
           prevmin = dict[i]['prev_min']
           return prevmin
        
         
        if getMin(color_data) != getPrevMin(color_data):
                print('The color ' + str(color_data[i]['color']) + ' minimum changed to: '+ str(color_data[i]['min']))
                          
        
        color_data[0]['prev_min']=min_b
        color_data[1]['prev_min']=min_r
        color_data[2]['prev_min']=min_g

        
        
                



        # Define os limites de cor com base nos valores das trackbars
        lower_bound = (min_b, min_g, min_r)
        upper_bound = (max_b, max_g, max_r)

         # Cria uma máscara para a detecção de cor
        mask = cv2.inRange(hsv, lower_bound, upper_bound)
 
        # Atualiza as janelas OpenCV
        frame_sized=cv2.resize(frame,(600,400))
        cv2.imshow('Original Image', cv2.flip(frame_sized,1))

        mask_sized=cv2.resize(mask,(600,400))
        cv2.imshow('Color Mask', cv2.flip(mask_sized,1))

        key = cv2.waitKey(1)
        if key == ord('w'):
            # Salva os limites em um arquivo JSON
            limits = {'limits': {'B': {'min': min_b, 'max': max_b}, 'G': {'min': min_g, 'max': max_g}, 'R': {'min': min_r, 'max': max_r}}}
        

            with open('limits.json', 'w') as file:
             json.dump(limits,file)
            
            print('Saved.....') 

        elif key == ord('q'):
            print('Interrupted.....')
            break

if __name__ == '__main__':
    main()
