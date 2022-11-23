class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        alicePos, bobPos = 0, len(plants) - 1
        aliceCan, bobCan = capacityA, capacityB
        
        refill = 0
        while alicePos <= bobPos:
            if alicePos == bobPos:
                if aliceCan < plants[alicePos] and bobCan < plants[bobPos]:
                    refill += 1
            else:
            
                if aliceCan < plants[alicePos]:
                    refill += 1
                    aliceCan = capacityA

                aliceCan -= plants[alicePos]

                if bobCan < plants[bobPos]:
                    refill += 1
                    bobCan = capacityB

                bobCan -= plants[bobPos]
            
            alicePos += 1
            bobPos -= 1
        
        return refill