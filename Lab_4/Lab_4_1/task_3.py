import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# шипы
num_points = 7
radius_outer = 2.0
radius_inner = 1.1
angles = np.linspace(0, 2*np.pi, num_points*2 + 1)
points = []
for i, angle in enumerate(angles):
    r = radius_outer if i % 2 == 0 else radius_inner
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    points.append((x, y))
star = patches.Polygon(points, closed=True, facecolor='#52307d', edgecolor='#3b1f54', linewidth=2)
ax.add_patch(star)

# тело и голова
center_circle = patches.Circle((0, 0), radius=1, facecolor='#d0507a', edgecolor='#7a2f48', linewidth=3)
ax.add_patch(center_circle)

# Глаза
eye_radius = 0.4
eye_white_left = patches.Circle((-0.4, 0.3), radius=eye_radius, facecolor='white', edgecolor='black', linewidth=1)
eye_white_right = patches.Circle((0.4, 0.3), radius=eye_radius, facecolor='white', edgecolor='black', linewidth=1)
ax.add_patch(eye_white_left)
ax.add_patch(eye_white_right)

# Зрачки
pupil_radius = 0.18
pupil_left = patches.Circle((-0.4, 0.38), radius=pupil_radius, facecolor='black')
pupil_right = patches.Circle((0.4, 0.38), radius=pupil_radius, facecolor='black')
ax.add_patch(pupil_left)
ax.add_patch(pupil_right)

highlight_radius = 0.07
highlight_left = patches.Circle((-0.35, 0.45), radius=highlight_radius, facecolor='white')
highlight_right = patches.Circle((0.45, 0.45), radius=highlight_radius, facecolor='white')
ax.add_patch(highlight_left)
ax.add_patch(highlight_right)

# Щечки
cheek_radius = 0.25
cheek_left = patches.Circle((-0.85, 0.1), radius=cheek_radius, facecolor='#c35370', edgecolor='#7a2f48', linewidth=2)
cheek_right = patches.Circle((0.85, 0.1), radius=cheek_radius, facecolor='#c35370', edgecolor='#7a2f48', linewidth=2)
ax.add_patch(cheek_left)
ax.add_patch(cheek_right)

# Нижние лапки
def draw_paw(x, y, width, height):
    paw = patches.Ellipse((x, y), width=width, height=height, facecolor='#c35370', edgecolor='#7a2f48', linewidth=2)
    ax.add_patch(paw)

draw_paw(-0.55, -0.7, 0.45, 0.7)  # Левая нижняя лапка
draw_paw(0.55, -0.7, 0.45, 0.7)   # Правая нижняя лапка

# Нос
nose = patches.Polygon([(-0.06, 0.0), (0.06, 0.0), (0, -0.1)], closed=True, facecolor='#7a2f48')
ax.add_patch(nose)

# Рот
mouth = patches.Polygon([(-0.05, -0.15), (0.05, -0.15), (0, -0.22)], closed=True, facecolor='#7a2f48')
ax.add_patch(mouth)

# Лимиты отображения
ax.set_xlim(-2.3, 2.3)
ax.set_ylim(-2.3, 2.3)

plt.savefig("hedgehog_updated_final.png")