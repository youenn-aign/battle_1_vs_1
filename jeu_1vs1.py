import pyxel
from typing import Tuple, List
from random import randint

WIDTH = 128																											
HEIGHT = 128
OBJ_SIZE = (6,8)
ecran_de_debut = True
#
JEU = True
coffre = False
deplacement_j1 = True
deplacement_j2 = True

image_0 = 0
image_1 = 1
image_2 = 2

(x_joueur1 ,y_joueur1) = (112, 104)
(x_joueur2 ,y_joueur2) = (8, 16)#(112, 112)

coffre_ouvert_ferme = [(48,40), (64,40)]
etat_coffre = 0
coordonne_coffre_apparition = [(43, 23), (67, 97), (4, 32), (116, 41), (4, 49), (116, 48), (4, 56), (116, 65), (4, 73), (116, 72), (4, 80), (116, 88), (4, 97), (116, 24), (37, 64), (83, 57)]
conteur_spawn_coffre = 0
#							'''bouclier''' 			'''soin'''					'''arme'''
position_contenu_coffre = [(48,0),(56,0),	(32,16),(40,16),(32,24),(40,24),	(48,8),(56,8),	(0,0)]#(,),(,),(,),(,),(,),(,),(,),]
conteur_contenu_coffre = 0
position_mini_item = 	  [(40,0),(40,8),	(00,00),(00,00),(00,00),(00,0),		(48,16),(56,16), (0,0)]

degats_joueur1 = 10
portee_joueur1 = 0
defense_joueur1 = 20 #%


degats_joueur2 = 10
portee_joueur2 = 0
defense_joueur2 = 20 #%

position_joueur1 = [ (16,16),(8,0),(16,0),(16,8),(16,24) ]
etat_joueur1 = 0
conteur_joueur1 = 4
item_joueur1 = -1
ancien_item1 = -1

position_joueur2 =  [ (0,8),(0,16),(8,8),(8,16),(0,24) ]#[ (0,72),(0,80),(8,80),(8,72),(0,88) ]
etat_joueur2 = 0
conteur_joueur2 = 4
item_joueur2 = -1
ancien_item2 = -1

vie_joueur1 = 200
vie_joueur2 = 200

score_joueur_1 = 0
score_joueur_2 = 0

etat_bombe1 = -1
etat_bombe2 = -1



ecriture_col = 7


def draw_ecran_de_debut() :
	pyxel.bltm(0,0,0,256,0,128,128)
	
	pyxel.line(0,64,128,64,0)
	pyxel.line(64,0,64,64,0)
	
	pyxel.text(17, 5, "PLAYER 2", 7)
	pyxel.text(81, 5, "PLAYER 1", 7)
	
	#pyxel.text(8, 96 - 29/2, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", ecriture_col)
	pyxel.text(64 - 18*2, 96 - 59/2, "LANCER UNE PARTIE :", ecriture_col)
	pyxel.text(64 - 6*2, 96 - 59/2 +6, "'SPACE'", ecriture_col)
	pyxel.text(64 - 15*2, 96 - 59/2+15, "QUITTER LE JEU :", ecriture_col)
	pyxel.text(64 - 10*2, 96 - 59/2+21, "'BACKSPACE'", ecriture_col)
	pyxel.text(64 - 20*2, 96 - 59/2+32, "SELECTIONNER LA MAP :", ecriture_col)
	pyxel.text(64 - 5*2, 96 - 59/2+40, "'NONE'", ecriture_col)
	pyxel.text(64 - 23*2, 96 - 59/2+49, "CHOISIR SON PERSONNAGE :", ecriture_col)
	pyxel.text(64 - 5*2, 96 - 59/2+55, "'NONE'", ecriture_col)

def draw_ecran_de_fin()	:
	pyxel.bltm(0,0,0,128,0,128,128)
	
	pyxel.line(0,64,128,64,0)
	
	if vie_joueur1 <= 0 and vie_joueur2 <= 0:
		pyxel.text(64-4*2, 15, "DRAW", 7)
		if score_joueur_2 > score_joueur_1 :
			pyxel.text(17, 25, "PLAYER 2", 7)
			pyxel.text(81, 25, "PLAYER 1", 7)
			pyxel.blt(27,14,image_0,35,41,10,8,5)
			pyxel.text(15, 35, f"SCORE : {score_joueur_2}", ecriture_col)
			pyxel.text(79, 35, f"SCORE : {score_joueur_1}", ecriture_col)
			
		elif score_joueur_1 > score_joueur_2 :
			pyxel.text(17, 25, "PLAYER 2", 7)
			pyxel.text(81, 25, "PLAYER 1", 7)
			pyxel.blt(91,14,image_0,35,41,10,8,5)
			pyxel.text(15, 35, f"SCORE : {score_joueur_2}", ecriture_col)
			pyxel.text(79, 35, f"SCORE : {score_joueur_1}", ecriture_col)
		
		else :
			pyxel.text(17, 25, "PLAYER 2", 7)
			pyxel.text(81, 25, "PLAYER 1", 7)
			pyxel.text(15, 35, f"SCORE : {score_joueur_2}", ecriture_col)
			pyxel.text(79, 35, f"SCORE : {score_joueur_1}", ecriture_col)
			
			
	else :
		pyxel.line(64,0,64,64,0)
		
		if vie_joueur1 <= 0 :
			pyxel.text(21, 15, "WINNER", pyxel . frame_count  %  16)
			pyxel.text(87, 15, "LOSER", 0)
			pyxel.text(17, 23, "PLAYER 2", pyxel . frame_count  %  16)
			pyxel.text(81, 23, "PLAYER 1", 0)
			#print(vie_joueur1,",",vie_joueur2)
			
			pyxel.text( 15, 35, f"SCORE : {score_joueur_2}", ecriture_col)
			pyxel.text( 79, 35, f"SCORE : {score_joueur_1}", ecriture_col)
			
			if score_joueur_2 > score_joueur_1 :
				pyxel.blt(27,45,image_0,35,41,10,8,5)
			elif score_joueur_1 > score_joueur_2 :
				pyxel.blt(91,45,image_0,35,41,10,8,5)
				
		elif vie_joueur2 <= 0 :
			pyxel.text(21, 15, "LOSER", 0)
			pyxel.text(87, 15, "WINNER", pyxel . frame_count  %  16)
			pyxel.text(17, 23, "PLAYER 2", 0)
			pyxel.text(81, 23, "PLAYER 1", pyxel . frame_count  %  16)
		
			pyxel.text( 15, 35, f"SCORE : {score_joueur_2}", ecriture_col)
			pyxel.text( 79, 35, f"SCORE : {score_joueur_1}", ecriture_col)
			
			if score_joueur_2 > score_joueur_1 :
				pyxel.blt(27,45,image_0,35,41,10,8,5)
			elif score_joueur_1 > score_joueur_2 :
				pyxel.blt(91,45,image_0,35,41,10,8,5)
	pyxel.text(64 - 25*2, 96 - 29/2, "POUR RELANCER UNE PARTIE :", ecriture_col)
	pyxel.text(64 - 6*2, 96 - 29/2 +6, "'SPACE'", ecriture_col)
	pyxel.text(64 - 20*2, 96 - 29/2+18, "POUR QUITTER LE JEU :", ecriture_col)
	pyxel.text(64 - 10*2, 96 - 29/2+24, "'BACKSPACE'", ecriture_col)

def draw_joueur_and_explosion(etat_bombe1, etat_bombe2, JEU, vie_joueur1, vie_joueur2, etat_joueur1, etat_joueur2, conteur_joueur1, conteur_joueur2, deplacement_j1, deplacement_j2) :

	if etat_bombe1 == -1:
		pyxel.blt(x_joueur1, y_joueur1, image_0, position_joueur1[etat_joueur1][0], position_joueur1[etat_joueur1][1], 8,8,5)
		barre_vie_joueur(vie_joueur1, x_joueur1, y_joueur1)
		conteur_joueur1 += 1
		
		if conteur_joueur1 == 3 :
			etat_joueur1 = 0
			conteur_joueur1 = 4

		if  pyxel.btn(pyxel.KEY_PAGEDOWN) :
			if 0<=item_joueur1<=1 :
				etat_joueur1 = 0
				#print("OUI")
			else :
				etat_joueur1 = 4
				#print("NON")
			deplacement_j1 = False
		else :
			etat_joueur1 = 0
			deplacement_j1 = True
	else:
		pyxel.blt(x_joueur1 - 4, y_joueur1 - 4,    1,    0 + etat_bombe1 * 16, 40,     16, 16,5)
		if etat_bombe1 != 11:
			etat_bombe1 += 1
		elif etat_bombe1 == 11:
			JEU = False
		
				
	if etat_bombe2 == -1:
		pyxel.blt(x_joueur2,y_joueur2,image_0,position_joueur2[etat_joueur2][0],position_joueur2[etat_joueur2][1],8,8,5)
		barre_vie_joueur(vie_joueur2, x_joueur2, y_joueur2)
		conteur_joueur2 += 1
		
		if conteur_joueur2 == 3 :
			etat_joueur2 = 0
			conteur_joueur2 = 4

		if  pyxel.btn(pyxel.KEY_G) :
			if 0<item_joueur2<1 :
				etat_joueur2 = 0
			else :
				etat_joueur2 = 4
			deplacement_j2 = False
		else :
			etat_joueur2 = 0
			deplacement_j2 = True
		
	else:
		pyxel.blt(x_joueur2 - 4, y_joueur2 - 4,    1,    0 + etat_bombe2 * 16, 40,     16, 16,5)
		if etat_bombe2 != 11:
			etat_bombe2 += 1
		elif etat_bombe2 == 11:
			JEU = False
			
			
	return (etat_bombe1, etat_bombe2, JEU, vie_joueur1, vie_joueur2, etat_joueur1, etat_joueur2, conteur_joueur1, conteur_joueur2, deplacement_j1, deplacement_j2)

def barre_vie_joueur(vie : int, x : int, y : int) :
	pyxel.blt(x-2, y-4, image_0, 48,48, 11,3, 5)
	vie = vie // 20 
	
	pyxel.blt(x-1, y-3, image_0, 73,75-vie, 9,1)
	#print(vie)
	
	
def attaque_1vers2(vie, defense_joueur2, degats_joueur1, portee_joueur1) -> int :
	if (x_joueur1 - 12 - portee_joueur1 <x_joueur2< x_joueur1 + 12 + portee_joueur1 and y_joueur1 - 12 - portee_joueur1 <y_joueur2< y_joueur1 + 12 + portee_joueur1):  
		vie = touche_defense_joueur2(vie, defense_joueur2, degats_joueur1)
		#print("J2",vie)
	return(vie)
	
def touche_defense_joueur2(vie, defense_joueur2, degats_joueur1) :
	if pyxel.btn(pyxel.KEY_G) :
		vie -= degats_joueur1/100*(100-defense_joueur2)
	else :
		vie -= degats_joueur1	
	return (vie)

	
def attaque_2vers1(vie, defense_joueur1, degats_joueur2, portee_joueur2) -> int :
	if (x_joueur2 - 12 - portee_joueur2 <x_joueur1< x_joueur2 + 12 + portee_joueur2 and y_joueur2 - 12 - portee_joueur2 <y_joueur1< y_joueur2 + 12 + portee_joueur2):
		vie = touche_defense_joueur1(vie, defense_joueur1, degats_joueur2)
		#print("J1",vie)
	return(vie)

def touche_defense_joueur1(vie, defense_joueur1, degats_joueur2) :
	if pyxel.btn(pyxel.KEY_PAGEDOWN) :
		vie -= degats_joueur2/100*(100-defense_joueur1)
	else :
		vie -= degats_joueur2
	return (vie)

def coffre_bonus(x1, y1, x2, y2, etat_coffre, random_coffre_coordonne, conteur_spawn_coffre, contenu_coffre, conteur_contenu_coffre, item_joueur1, item_joueur2, ancien_item1, ancien_item2) :

	pyxel.blt(coordonne_coffre_apparition[random_coffre_coordonne][0],coordonne_coffre_apparition[random_coffre_coordonne][1], image_0, coffre_ouvert_ferme[etat_coffre][0],coffre_ouvert_ferme[etat_coffre][1], 8,8, 5)

	conteur_spawn_coffre += 1
	
	if pyxel.btnp(pyxel.KEY_KP_ENTER) or pyxel.btnp(pyxel.KEY_PAGEUP) and etat_coffre == 0:
		if x1-8<coordonne_coffre_apparition[random_coffre_coordonne][0]<x1+7 and y1-8<coordonne_coffre_apparition[random_coffre_coordonne][1]<y1+9 :
			etat_coffre = 1
			conteur_spawn_coffre = 0
			ancien_item1 = item_joueur1
			item_joueur1 = contenu_coffre
		
			
	if pyxel.btnp(pyxel.KEY_H) and etat_coffre == 0:
		if x2-8<coordonne_coffre_apparition[random_coffre_coordonne][0]<x2+7 and y2-8<coordonne_coffre_apparition[random_coffre_coordonne][1]<y2+9 :
			etat_coffre = 1
			conteur_spawn_coffre = 0
			ancien_item2 = item_joueur2
			item_joueur2  = contenu_coffre
			

	if etat_coffre == 1 and conteur_spawn_coffre >= 75:
		random_coffre_coordonne_anciens = random_coffre_coordonne
		random_coffre_coordonne = randint(0, 15)

		while random_coffre_coordonne_anciens == random_coffre_coordonne :
			random_coffre_coordonne = randint(0, 15)
			
		etat_coffre = 0
	(contenu_coffre, conteur_contenu_coffre) = contenu_coffre_bonus(etat_coffre, random_coffre_coordonne, contenu_coffre, conteur_contenu_coffre)
	
	return (etat_coffre, random_coffre_coordonne, conteur_spawn_coffre, contenu_coffre, conteur_contenu_coffre, item_joueur1, item_joueur2, ancien_item1, ancien_item2)

def contenu_coffre_bonus(etat_coffre, random_coffre_coordonne, contenu_coffre, conteur_contenu_coffre):
	if etat_coffre == 1 and conteur_contenu_coffre <= 10:
		pyxel.blt(coordonne_coffre_apparition[random_coffre_coordonne][0], coordonne_coffre_apparition[random_coffre_coordonne][1] - conteur_contenu_coffre, image_0,position_contenu_coffre[contenu_coffre][0],position_contenu_coffre[contenu_coffre][1], 8,8, 5)
		conteur_contenu_coffre += 1
		
	if etat_coffre == 1 and 10 < conteur_contenu_coffre < 30:
		pyxel.blt(coordonne_coffre_apparition[random_coffre_coordonne][0], coordonne_coffre_apparition[random_coffre_coordonne][1] - 10, image_0,position_contenu_coffre[contenu_coffre][0],position_contenu_coffre[contenu_coffre][1], 8,8, 5)
		conteur_contenu_coffre += 1
		
	if etat_coffre == 0 :
		contenu_coffre = randint(0, 7)
		conteur_contenu_coffre = 0
	return (contenu_coffre, conteur_contenu_coffre)


def deplacement_joueur1(x : int, y : int, bordure : List, etat_joueur1 : int, conteur_joueur1)  :
	if pyxel.btn(pyxel.KEY_RIGHT) and bordure[2] :
		if (x < WIDTH - OBJ_SIZE[0]):
			x += 1
			etat_joueur1 = 3
			conteur_joueur1 = 0
	if pyxel.btn(pyxel.KEY_LEFT) and bordure[0]  :
		if (x > 0) :
			x -= 1
			etat_joueur1 = 2
			conteur_joueur1 = 0
	if pyxel.btn(pyxel.KEY_DOWN) and bordure[1] :
		if (y < HEIGHT - OBJ_SIZE[1])  :
			y += 1
			etat_joueur1 = 0
			conteur_joueur1 = 4
	if pyxel.btn(pyxel.KEY_UP) and bordure[3] :
		if (y > 0) :
			y -= 1
			etat_joueur1 = 1
			conteur_joueur1 = 4
	
	return (x, y, etat_joueur1, conteur_joueur1)
	
def deplacement_joueur2(x : int, y : int, bordure : List, etat_joueur2 : int, conteur_joueur2)  :
	if pyxel.btn(pyxel.KEY_D) and bordure[2]:
		if (x < WIDTH - OBJ_SIZE[0]):
			x += 1
			etat_joueur2 = 3
			conteur_joueur2 = 0
	if pyxel.btn(pyxel.KEY_Q) and bordure[0] :
		if (x > 0) :
			x -= 1
			etat_joueur2 = 2
			conteur_joueur2 = 0
	if pyxel.btn(pyxel.KEY_S) and bordure[1]:
		if (y < HEIGHT - OBJ_SIZE[1])  :
			y += 1
			etat_joueur2 = 0
			conteur_joueur2 = 4
	if pyxel.btn(pyxel.KEY_Z) and bordure[3] :
		if (y > 0) :
			y -= 1
			etat_joueur2 = 1
			conteur_joueur2 = 4
			
	return (x, y, etat_joueur2, conteur_joueur2)
	
def bordure_map(x, y, cote) :
	bloquage = []
	for pixel in range(len(cote)):
		x1 = cote[pixel][0]
		y1 = cote[pixel][1]
		color = pyxel.pget(x1, y1)
		if color == 1 :
			bloquage.append(False)
		elif color == 13 :
			bloquage.append(False)
		else :
			bloquage.append(True)
	if False in bloquage :
		passage = False
	else :
		passage = True
	return passage

def item_bonus_joueur(item_joueur, vie, defense, x, y, ancien_item, degats, portee) :
	
	if item_joueur == 0 :
		degats = 10
		portee = 0
		defense = 40

	elif item_joueur == 1 :
		degats = 10
		portee = 0
		defense = 60
		
	elif item_joueur == 2 :
		vie += 25
		if vie > 200 :
			vie = 200
		item_joueur = ancien_item
		
	elif item_joueur == 3:
		vie += 50
		if vie > 200 :
			vie = 200
		item_joueur = ancien_item

	elif item_joueur == 4 :
		vie += 75
		if vie > 200 :
			vie = 200
		item_joueur = ancien_item

	elif item_joueur == 5 :
		vie += 100
		if vie > 200 :
			vie = 200
		item_joueur = ancien_item
		
	elif item_joueur == 6 :
		defense = 20
		degats = 40
		portee = 4

	elif item_joueur == 7 :
		defense = 20
		degats = 25
		portee = 10
		
	else :
		degats = 10
		defense = 20
		portee = 0
		
	return (item_joueur, vie, defense, ancien_item, degats, portee)

def draw_item_joueur(item_joueur, x, y) :
	if item_joueur == 0 and pyxel.btn(pyxel.KEY_PAGEDOWN) or pyxel.btn(pyxel.KEY_G) :
		pyxel.blt(x, y+1, image_0, position_mini_item[item_joueur][0], position_mini_item[item_joueur][1], 8, 8, 5)
		
	if item_joueur == 1 and pyxel.btn(pyxel.KEY_PAGEDOWN) or pyxel.btn(pyxel.KEY_G):
		pyxel.blt(x, y+1, image_0, position_mini_item[item_joueur][0], position_mini_item[item_joueur][1], 8, 8, 5)

	if item_joueur == 6 :
		pyxel.blt(x, y+1, image_0, position_mini_item[item_joueur][0], position_mini_item[item_joueur][1], 8, 8, 5)

	if item_joueur == 7 :
		pyxel.blt(x, y+1, image_0, position_mini_item[item_joueur][0], position_mini_item[item_joueur][1], 8, 8, 5)
	


def draw():
	global etat_bombe1, etat_bombe2, JEU, vie_joueur1, vie_joueur2, ecran_de_debut, etat_joueur1, etat_joueur2, position_joueur1, position_joueur2, conteur_joueur1, conteur_joueur2, bordure_joueur1, bordure_joueur2, etat_coffre, random_coffre_coordonne, conteur_spawn_coffre, contenu_coffre, conteur_contenu_coffre, item_joueur1, item_joueur2, deplacement_j1, deplacement_j2, position_mini_item, ancien_item1, ancien_item2
	
	if ecran_de_debut :
		draw_ecran_de_debut()
		
	else :	
		if JEU :
			pyxel.bltm(0,0,0,0,0*8,128,128)
			(etat_coffre , random_coffre_coordonne, conteur_spawn_coffre, contenu_coffre, conteur_contenu_coffre, item_joueur1, item_joueur2, ancien_item1, ancien_item2) = coffre_bonus(x_joueur1, y_joueur1, x_joueur2, y_joueur2, etat_coffre, random_coffre_coordonne, conteur_spawn_coffre, contenu_coffre, conteur_contenu_coffre, item_joueur1, item_joueur2, ancien_item1, ancien_item2)
			
			(etat_bombe1, etat_bombe2, JEU, vie_joueur1, vie_joueur2, etat_joueur1, etat_joueur2, conteur_joueur1, conteur_joueur2,deplacement_j1, deplacement_j2) = draw_joueur_and_explosion(etat_bombe1, etat_bombe2, JEU, vie_joueur1, vie_joueur2, etat_joueur1, etat_joueur2, conteur_joueur1, conteur_joueur2,deplacement_j1, deplacement_j2)

			draw_item_joueur(item_joueur1, x_joueur1, y_joueur1)
			draw_item_joueur(item_joueur2, x_joueur2, y_joueur2)
			
		else :
			draw_ecran_de_fin()
		
		

def update():
	global x_joueur1 ,y_joueur1, x_joueur2 , y_joueur2, vie_joueur1, vie_joueur2, JEU, score_joueur_1, score_joueur_2, ecran_de_debut, etat_bombe1, etat_bombe2, etat_joueur1, etat_joueur2, conteur_joueur1, conteur_joueur2, item_joueur1, item_joueur2, deplacement_j1, deplacement_j2, defense_joueur1, defense_joueur2,ancien_item1, ancien_item2, degats_joueur1, degats_joueur2, portee_joueur1, portee_joueur2
	if ecran_de_debut :
		if pyxel.btnp(pyxel.KEY_SPACE):
			ecran_de_debut = False
			
	if pyxel.btnp(pyxel.KEY_BACKSPACE):
				pyxel.quit()
				
	else :
		if JEU :
			#print("def j1" , defense_joueur1, "        def j2", defense_joueur2,"deg j1" , degats_joueur1, "        deg j2", degats_joueur2)
			#print(etat_joueur1)
			
			cote_gauche_joueur1 = []
			cote_bas_joueur1 = []
			cote_droit_joueur1 = []
			cote_haut_joueur1 = []

			for i in range(8):
				cote_gauche_joueur1.append((x_joueur1,y_joueur1+i))
			for i in range(5):
				cote_bas_joueur1.append((x_joueur1+1+i,y_joueur1+8))
			for i in range(8):
				cote_droit_joueur1.append((x_joueur1+6,y_joueur1+i))
			for i in range(5):
				cote_haut_joueur1.append((x_joueur1+1+i,y_joueur1-1))

			cote_gauche_joueur2 = []
			cote_bas_joueur2 = []
			cote_droit_joueur2 = []
			cote_haut_joueur2 = []

			for i in range(8):
				cote_gauche_joueur2.append((x_joueur2,y_joueur2+i))
			for i in range(5):
				cote_bas_joueur2.append((x_joueur2+1+i,y_joueur2+8))
			for i in range(8):
				cote_droit_joueur2.append((x_joueur2+6,y_joueur2+i))
			for i in range(5):
				cote_haut_joueur2.append((x_joueur2+1+i,y_joueur2-1))
			
			bordure_joueur1 = []
			bordure_joueur2 = []
			
			bordure_joueur1.append(bordure_map(x_joueur1 ,y_joueur1, cote_gauche_joueur1))
			bordure_joueur1.append(bordure_map(x_joueur1 ,y_joueur1, cote_bas_joueur1))
			bordure_joueur1.append(bordure_map(x_joueur1 ,y_joueur1, cote_droit_joueur1))
			bordure_joueur1.append(bordure_map(x_joueur1 ,y_joueur1, cote_haut_joueur1))

			bordure_joueur2.append(bordure_map(x_joueur2 ,y_joueur2, cote_gauche_joueur2))
			bordure_joueur2.append(bordure_map(x_joueur2 ,y_joueur2, cote_bas_joueur2))
			bordure_joueur2.append(bordure_map(x_joueur2 ,y_joueur2, cote_droit_joueur2))
			bordure_joueur2.append(bordure_map(x_joueur2 ,y_joueur2, cote_haut_joueur2))
			#print(bordure_joueur1)

			if etat_bombe1 == -1 and etat_bombe2 == -1 :
				if deplacement_j1 :
					(x_joueur1 ,y_joueur1, etat_joueur1, conteur_joueur1) = deplacement_joueur1(x_joueur1 ,y_joueur1, bordure_joueur1, etat_joueur1, conteur_joueur1)
				if deplacement_j2 :
					(x_joueur2 ,y_joueur2, etat_joueur2, conteur_joueur2) = deplacement_joueur2(x_joueur2 ,y_joueur2, bordure_joueur2, etat_joueur2, conteur_joueur2)

				(item_joueur1, vie_joueur1, defense_joueur1, ancien_item1, degats_joueur1, portee_joueur1) = item_bonus_joueur(item_joueur1, vie_joueur1, defense_joueur1, x_joueur1, y_joueur1, ancien_item1, degats_joueur1, portee_joueur1)
				(item_joueur2, vie_joueur2, defense_joueur2, ancien_item2, degats_joueur2, portee_joueur2) = item_bonus_joueur(item_joueur2, vie_joueur2, defense_joueur2, x_joueur2, y_joueur2, ancien_item2, degats_joueur2, portee_joueur2)
				
			
				if pyxel.btnp(pyxel.KEY_KP_ENTER) or pyxel.btnp(pyxel.KEY_PAGEUP) and deplacement_j1 :
					vie_joueur2 = attaque_1vers2(vie_joueur2, defense_joueur2, degats_joueur1, portee_joueur1)
					coffre = True
				#print("J2",vie_joueur2)
				
				if pyxel.btnp(pyxel.KEY_H) and deplacement_j2:
					vie_joueur1 = attaque_2vers1(vie_joueur1, defense_joueur1, degats_joueur2, portee_joueur2)
					coffre = True
				#print("J1",vie_joueur1)
			
			if vie_joueur1 <= 0 and etat_bombe1 == -1:
				etat_bombe1 = 0
				score_joueur_2 += 1
				
				
			elif vie_joueur2 <= 0 and etat_bombe2 == -1 :
				etat_bombe2 = 0
				score_joueur_1 += 1
					
					
		else :
			
			
			if pyxel.btnp(pyxel.KEY_SPACE):
				vie_joueur1 = 200
				vie_joueur2 = 200
				
				(x_joueur1 ,y_joueur1) = (112, 104)
				(x_joueur2 ,y_joueur2) = (8, 16)#(112, 112)

				degats_joueur1 = 20
				defense_joueur1 = 25
				portee_joueur1 = 0
				item_joueur1 = -1
				ancien_item1 = -1
				
				degats_joueur2 = 20
				defense_joueur2 = 25
				portee_joueur2 = 0
				item_joueur2 = -1
				ancien_item2 = -1

				
				etat_bombe1 = -1
				etat_bombe2 = -1

				etat_coffre = 0
				
				etat_joueur2 = 0
				etat_joueur1 = 0
				
				JEU = True
	
if __name__ == "__main__":
	pyxel.init(WIDTH, HEIGHT, title="NDC 2023", fps=25)
	pyxel.load("texture.pyxres" )
	pyxel.tilemap(0)
	contenu_coffre = randint(0, 7)
	random_coffre_coordonne = randint(0, 15)
	JEU=pyxel.run(update, draw)
