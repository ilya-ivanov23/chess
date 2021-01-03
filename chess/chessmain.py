import pygame as p


WIDTH = HEIGHT = 512 #400 is another option
DIMENSION = 8 #dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DEMENSION
MAX_FPS = 15 #for animations later on
IMAGES = {}

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
    IMAGES[piece]= p.transform.scale(p.image.load("images/" + piece + ".png"),(SQ_SIZE,SQ_SIZE))
    #Note: we can access an image by saing 'IMAGES['wp']'

    def main():
        p.init()
        screen = p.display.set_mode((WIDTH, HEIGHT))
        clock = p.time.Clock()
        screen.fill(p.Color("white"))
        gs = chessengine.GameState()
        loadImages() #only do this once, before the while loop
        running = True
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                    drawGameState(screen, gs)
                    clock.tick(MAX_FPS)
                    p.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on the board
    #add in piece highlighting or move suggestions (later)
    drawPieces(screen, gs,board)#draw pieces on top of those squares

    def drawBoard(screen):
        colors = [p.Color("white"), p.Color("gray")]
        for r in range(DIMENSION):
              for c in range(DIMENSION):
                  color = colors[(r+c) % 2)]
                  p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
               
    def drawPieces(screen,board):
        for r in range(DIMENSION):
            for c in range(DIMENSION):
                piece = board[r][c]
                if piece != "--": #not empty square
                    screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    
                    
if __name__ == "__main__":
        main()







    





