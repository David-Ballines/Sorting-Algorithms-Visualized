import pygame
import random

pygame.init()
width = 900
height = 450
window = pygame.display.set_mode((width, height))
fnt1 = pygame.font.SysFont("comicsans", 30, bold=False, italic=False)
run = True

alg = "Pick an algorithm"

numbers = [0]*150
colors = [0]*150
colorPick = [(0,204,102), (255,0,0)]
size = 150

#might not need gap
gap = 4

class button():
    def __init__(self, color, x, y, width, height, text =""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    
    def draw(self,window,outline = None):
        if outline:
            pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != "":
            font = pygame.font.SysFont("comicsans",20)
            text = font.render(self.text,1, (0,0,0))
            window.blit(text, (self.x +(self.width/2 - text.get_width()/2),self.y + (self.height/2-text.get_height()/2)))

    def isOver(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if(pos[1] > self.y and pos[1] < self.y + self.height):
                return True
        
        return False
#might want to make this function to make it more efficient
def swap():
    pass 

#makes a new array 
def generate():
    for i in range(size):
        colors[i] = (0, 204, 102)
        numbers[i] = random.randrange(1,150)

#makes screen white then draws the lines again when calling draw
#do not need any of this
def refill():
    window.fill((255,255,255))
    draw()
    pygame.display.update()
    pygame.time.delay(50)

def bubbleSort(nums):
    for i in range(size):
        colors[0] = colorPick[1]
        for j in range(size - i-1):
            colors[j+1] = colorPick[1]
            refill()
            if(nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
            colors[j] = colorPick[0]
        colors[len(colors)-1-i] = colorPick[0]


def mergeDraw():
    pass


def mergeSort(l, r):
    mid = (l+r)//2
    if(l < r):
        mergeSort(l,mid)
        mergeSort(mid +1,r)
        merge(l, mid, mid +1,r)

def merge(x1, y1, x2, y2):
    i = x1
    j = x2
    temp = []
    pygame.event.pump()
    while i <= y1 and j <= y2:
        colors[i] = (255,0,0)
        colors[j] = (255,0,0)
        refill()
        colors[i] = (0,204,102)
        colors[j] = (0,204,102)
        if(numbers[i] < numbers[j]):
            temp.append(numbers[i])
            i += 1
        else:
            temp.append(numbers[j])
            j += 1
    while i <= y1:
        colors[i] = (225,0,0)
        refill()
        colors[i] = (0,204,102)
        temp.append(numbers[i])
        i +=1
    while j <= y2:
        colors[j] = (255,0,0)
        refill()
        colors[j] = (0,204,102)
        temp.append(numbers[j])
        j += 1
    j = 0
    for i in range(x1, y2 +1):
        pygame.event.pump()
        numbers[i] = temp[j]
        j+=1
        refill()
        #if (y2 - x1 == len(numbers)-2):


def partition(l, r):
    i = l-1
    pivot = numbers[r]
    colors[r] = (255,0,0)
    refill()
    for j in range(l,r):
        if(numbers[j] < pivot):
            i +=1
            refill()
            numbers[i], numbers[j] = numbers[j],numbers[i]
    refill()
    numbers[i+1], numbers[r] = numbers[r],numbers[i+1]
    refill() 
    return(i+1)

def quickSort(l, r):
    if(l < r):
        part = partition(l,r)
        
        quickSort(l,part-1)
        quickSort(part+1,r)

def draw():
    #might need to draw some text
    txt1 = fnt1.render(alg,1,(0,0,0))
    window.blit(txt1,(600,60))
    lineWidth = (width -150)//size
    boundaryArr = 900/size
    boundaryGrp = 550/100

    mergeButton.draw(window)
    bubbleButton.draw(window)
    quickButton.draw(window)
    generateButton.draw(window)

    #makes the black bar that divides the words and arrays
    pygame.draw.line(window,(0,0,0), 
                    (0,95),
                    (900,95),6)

    for i in range(1,size):
        pygame.draw.line(window, colors[i],
                        (boundaryArr*i-3,height),
                        (boundaryArr*i-3,height - numbers[i]*2),lineWidth)

generate()

mergeButton = button((219,202,47), 20,20,100,70,"Merge Sort")

bubbleButton = button((219,202,47),140,20,100,70, "Bubble Sort")

quickButton = button((219, 202,47), 260,20,100,70, "Quick Sort")

generateButton = button((219,202,47), 380,20,100,70,"Make New Array")


while run:
    window.fill((255,255,255))
    for event in pygame.event.get():
        position = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                quickSort(1, len(numbers)-1)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(mergeButton.isOver(position)):
                alg = "algorithm used: Merge Sort"
                mergeSort(0,len(numbers)-1)
            if(quickButton.isOver(position)):
                alg = "algorithm used: Quick Sort"
                quickSort(0, len(numbers)-1)
            if(bubbleButton.isOver(position)):
                alg = "algorithm used: Bubble Sort"
                bubbleSort(numbers)
            if(generateButton.isOver(position)):
                generate()
                alg = "Pick an algorithm"
    draw()
    pygame.display.update()

pygame.quit()