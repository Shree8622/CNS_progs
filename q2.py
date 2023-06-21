from time import sleep
import random
import threading

def GeneratePacket(bucket):
    item = random.randint(0,10)
    bucket.append(item)
    print("Packet appended to bucket")

def ConstantPacketGenerator(bucket):
    n=10
    while n:
        GeneratePacket(bucket)
        print("Bucket state: ",bucket)
        sleep(1)
        n-=1
        
def BurstPacketGenerator(bucket):
    n=3
    while n:
        for i in range(3):
            GeneratePacket(bucket)
        print("Bucket state: ",bucket)
        n-=1
        sleep(0.2)


def PopPacket(bucket:list):
    while len(bucket)>0:
        bucket.pop()
        print("Element popped \nBucket state: ",bucket)
        sleep(1)
    else:
        print("Bucket is empty!")

if __name__ == '__main__':
    bucket=[]
    ConstantPacketGen = threading.Thread(target=ConstantPacketGenerator,args=(bucket,))
    BurstPacketGen = threading.Thread(target=BurstPacketGenerator,args=(bucket,))
    PacketPop = threading.Thread(target=PopPacket,args=(bucket,))
    ConstantPacketGen.start()
    BurstPacketGen.start()
    PacketPop.start()
