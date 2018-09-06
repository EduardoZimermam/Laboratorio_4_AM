#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn import datasets
import os
import cv2

# Método para carregar o Digits Dataset e gerar o arquivo de caracteristicas.
def loadDigitsDataset():
	os.system("python digits.py")

	X_data_digits, y_target_digits = datasets.load_svmlight_file('features.txt')	

	return X_data_digits, y_target_digits


# x, Y = loadDigitsDataset();


# Template Matching
# Concavidades
# Momentos de HU

img = cv2.imread('teste.tif', 0)
template = cv2.imread('template.tif', 0)

res = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)

print(res)