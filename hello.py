print "Hello, World!"

import random

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Dice dot positions for each face
dice_faces = {
    1: [(0.5, 0.5)],
    2: [(0.25, 0.25), (0.75, 0.75)],
    3: [(0.25, 0.25), (0.5, 0.5), (0.75, 0.75)],
    4: [(0.25, 0.25), (0.25, 0.75), (0.75, 0.25), (0.75, 0.75)],
    5: [(0.25, 0.25), (0.25, 0.75), (0.5, 0.5), (0.75, 0.25), (0.75, 0.75)],
    6: [(0.25, 0.25), (0.25, 0.5), (0.25, 0.75), (0.75, 0.25), (0.75, 0.5), (0.75, 0.75)]
}

def draw_dice(face):
    plt.clf()
    ax = plt.gca()
    ax.set_aspect('equal')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, fill=True, color='white', edgecolor='black'))
    for x, y in dice_faces[face]:
        ax.add_patch(patches.Circle((x, y), 0.08, color='black'))
    plt.draw()
    plt.pause(0.1)

plt.ion()
plt.figure(figsize=(2,2))

# Animate dice roll
for _ in range(10):
    draw_dice(random.randint(1, 6))

# Final result
final_face = random.randint(1, 6)
draw_dice(final_face)
print(f"You rolled a {final_face}!")
plt.ioff()
plt.show()