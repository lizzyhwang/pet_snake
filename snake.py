# class that represents the snake on the screen
from typing import List
import random

class Snake:
    # body is list of segments. a segment is a tuple (x,y) where x and y are tile coordinates in the map.
    # tile (0,0) is the top left of the window.
    # the map is set to 720 x 720 px
    # each tile is 40 x 40 px, which means the grid is 18 x 18.

    # initialize attributes
    body = []
    numTiles = 0
    def __init__(self, ts, ws) -> None:
        # X X X X
        #       X
        #   X X X
        #   X
        #   X X X X X X X
        self.body = [
            (3,4),(4,4),(5,4),(6,4),(6,5),(6,6),(5,6),(4,6),(4,7),(4,8),(5,8),(6,8),(7,8),(8,8),(9,8),(10,8)
        ]
        self.numTiles = ws/ts

    # returns the body segment at the given index -> (x,y)
    def getSegment(self, idx: int):
        return self.body[idx]

    # returns the head segment -> (x,y)
    def getHead(self):
        return self.body[0];

    # removes the tail -> void
    def removeTail(self):
        self.body = self.body[:-1]

    # removes the old tail, adds a new head -> void
    def addHead(self):
        self.removeTail()
        head = self.getHead()
        x = head[0]
        y = head[1]
        # allowed moves
        potentialHeads = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        toRemove = []
        for p in potentialHeads:
            # remove if the new move is the current neck so it doesnt go back on itself too much
            if p == self.getSegment(1):
                toRemove.append(p)
            # remove if it would be out of bounds.
            pX = p[0]
            pY = p[1]
            if pX < 0 or pX >= self.numTiles or pY < 0 or pY >= self.numTiles:
                toRemove.append(p)
        # remove the bad moves from the list of moves
        for s in toRemove:
            potentialHeads.remove(s)
        # pick a new head from the list of moves
        newHead = random.choice(potentialHeads)
        # insert the new head
        self.body.insert(0,newHead)