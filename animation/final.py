import pgzrun

WIDTH = 650
HEIGHT = 500

alien = Actor("alien")
alien.pos = (0, HEIGHT / 2)

vx_a = 6 # vitesse x de mon sprite
vy_a = 6 # vitesse y de mon sprite
 
def draw():
    screen.clear()
    alien.draw()
 
 
def update():
    global vx_a, vy_a
    
    if (alien.x < 0 or alien.x > WIDTH):
        vx_a = -vx_a # change la direction (x)
    if (alien.y < 0 or alien.y > HEIGHT):
        vy_a = -vy_a #change la direction (y)
    
    alien.x += vx_a
    alien.y += vy_a        
 
 
score = 0
#C'est le score fixé qui sera le score au début du jeu
 
def on_mouse_down(pos):
    global score
    if alien.collidepoint(pos):
        set_alien_hit()
        score += 1
        print(score)
    else:
        score -= 1
        print(score)
#La commande qui s'occupe du score.
#Ainsi, chaque fois que vous cliquez sur l'extraterrestre, vous gagnez 1 point,
#mais si vous cliquez mal sur l'écran noir, vous perdez 1 point, c'est un jeu de suivi
def set_alien_hit():
    alien.image = 'alien_hurt'
    clock.schedule_unique(set_alien_normal, 0.5) 
# L'ordre de changer l'étranger normal en étranger blessé après avoir cliqué sur lui
 
def set_alien_normal():
    alien.image = 'alien'
#La commande de réinitialisation pour qu'après 0,5 seconde, l'image extraterrestre normale revienne
pgzrun.go()