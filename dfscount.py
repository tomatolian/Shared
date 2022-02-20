from PIL import Image
import numpy as np
import sys
sys.setrecursionlimit(2000) #画像が大きすぎて最大再帰回数が多すぎるので、1000->2000に変更
grid=np.array(Image.open('target.jpg').convert('L'))#グレースケールにして二次元化
grid=np.where(grid<100,0,1) #2値化
N = grid.shape[0] 
M = grid.shape[1]
pil_img = Image.fromarray((grid*255).astype(np.uint8))
pil_img.save('test.png') #入力する画像
#深さ優先探索
def dfs(x,y):
    grid[x][y]=1 #現在の位置を1にする
    for i in range(-1, 2): #8近傍を探索
        for j in range(-1, 2): 
            if 0 <= x+i < N and 0 <= y+j < M and grid[x+i][y+j]== 0: #近くに0があったら
                dfs(x+i, y+j) #再帰する
count=0
while 0 in grid:
    t=np.unravel_index(np.argmax(grid==0), grid.shape) #次に探索する0の位置を決定
    x = t[0]
    y = t[1]
    dfs(x,y)
    count+=1
print(count)
