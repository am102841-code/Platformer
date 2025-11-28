# --- Input ---
keys = pygame.key.get_pressed()
player.vel_x = 0
if keys[pygame.K_LEFT]:
    player.vel_x = -player.move_speed
    player.player_now = player.player_image
    player.facing_left = True
if keys[pygame.K_RIGHT]:
    player.vel_x = player.move_speed
    player.player_now = player.player_flipped_image
    player.facing_left = False
if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and player.on_ground:
    player.vel_y = player.jump_strength
    player.on_ground = False

# --- Horizontal movement and collision ---
player.x += player.vel_x
player.hitbox.topleft = (player.x, player.y)
horizontal_collision(player, obstacle_list)

# --- Vertical movement and collision ---
player.vel_y += player.gravity
player.y += int(player.vel_y)
player.hitbox.topleft = (player.x, player.y)

player.on_ground = False
for ob in obstacle_list:
    if player.hitbox.colliderect(ob):
        if player.vel_y > 0 and player.hitbox.bottom - player.vel_y <= ob.top:
            player.y = ob.top - player.hitbox.height
            player.vel_y = 0
            player.on_ground = True
        elif player.vel_y < 0 and player.hitbox.top - player.vel_y >= ob.bottom:
            player.y = ob.bottom
            player.vel_y = 0
player.hitbox.topleft = (player.x, player.y)

