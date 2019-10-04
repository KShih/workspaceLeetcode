"""
(1,1) (3,5) -> True
(1,1) (2,3) -> True
(2,1) (1,1) -> False
(2,1) (1,0) -> False
(1,1) (2,5) -> True
(1,1) (3,6) -> False
"""

def BReachingPoint(sx, sy, tx, ty):
    if sx > tx or sy > ty:
         return False
    if sx == tx and sy == ty:
         return True

    if (ReachingPoint(sx+sy, sy, tx, ty)):
        return True
    else:
        return ReachingPoint(sx, sx+sy, tx, ty)

def ReachingPoint(sx, sy, tx, ty):
    print("tx=", tx)
    print("ty=", ty)
    if sx > tx or sy > ty:
        return False
    if sx == tx and (ty-sy) % sx == 0:
        return True
    if sy == ty and (tx-sx) % sy == 0:
        return True

    return ReachingPoint(sx, sy, tx%ty, ty%tx)


if __name__ == "__main__":
    print(ReachingPoint(1,1,3,5))
    print(ReachingPoint(1,1,2,3))
    print(ReachingPoint(2,1,1,1))
    print(ReachingPoint(2,1,1,0))
    print(ReachingPoint(1,1,2,5))
    print(ReachingPoint(1,1,3,6))
