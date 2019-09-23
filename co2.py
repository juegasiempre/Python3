import time
import readline

path = '/home/905634/ansible_dmvpn/co2_log.txt'
breathe = 120

hold = input("What's your current breath hold time in seconds?: ")
for x in range(0,8):
	print('\nBreathe for {} seconds until {}'.format(breathe,time.ctime(time.time()+breathe))) 
	time.sleep(breathe-10)
	print("\nYou're going to hold your breath in 10 seconds")
	time.sleep(5)
	print("\nYou're going to hold your breath in 5 seconds")
	time.sleep(1)
	print("\nYou're going to hold your breath in 4 seconds")
	time.sleep(1)
	print("\nYou're going to hold your breath in 3 seconds")
	time.sleep(1)
	print("\nYou're going to hold your breath in 2 seconds")
	time.sleep(1)
	print("\nYou're going to hold your breath in 1 second")
	time.sleep(1)
	print('\nHold for {} seconds until {}'.format((int(hold)/2),time.ctime(time.time()+(int(hold)/2))))
	breathe -= 15
	time.sleep(int(hold)/2)

f = open(path,'a')
f.write('Completed at {}        '.format(time.ctime(time.time())))
f.write(input('Did you finish?  What notes do you have? '))
f.write('\n')
f.close()

print("\nCongrats, you're one step close to becoming a fish")

