scene.set_background_color(8)
spaceplane=sprites.create(assets.image("""player"""),SpriteKind.player)
info.set_life(3)
spaceplane.set_stay_in_screen(True)
controller.move_sprite(spaceplane, 200, 200)
def on_a_pressed():
    missile=sprites.create_projectile_from_sprite(assets.image("""missile"""), spaceplane, 200, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED,
 on_a_pressed)    
def on_update():
    bogy=sprites.create(assets.image("""bogy"""),SpriteKind.enemy)
    bogy.set_velocity(-100, randint(-30, 30))
    bogy.y=randint(0, scene.screen_height())
    bogy.left=scene.screen_width()
    bogy.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update)   
def on_hit(sprite, othersprite):
    othersprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy,on_hit)    
def on_crash(sprite, othersprite):
    othersprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy,on_crash)    