from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class ItemLevel(SQLModel, table=True):
    __tablename__ = "item_level"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    strength: int
    dexterity: int
    vitality: int
    intelligence: int
    mind: int
    piety: int
    h_p: int
    m_p: int
    t_p: int
    g_p: int
    c_p: int
    physical_damage: int
    magical_damage: int
    delay: int
    additional_effect: int
    attack_speed: int
    block_rate: int
    block_strength: int
    tenacity: int
    attack_power: int
    defense: int
    direct_hit_rate: int
    evasion: int
    magic_defense: int
    critical_hit_power: int
    critical_hit_resilience: int
    critical_hit: int
    critical_hit_evasion: int
    slashing_resistance: int
    piercing_resistance: int
    blunt_resistance: int
    projectile_resistance: int
    attack_magic_potency: int
    healing_magic_potency: int
    enhancement_magic_potency: int
    enfeebling_magic_potency: int
    fire_resistance: int
    ice_resistance: int
    wind_resistance: int
    earth_resistance: int
    lightning_resistance: int
    water_resistance: int
    magic_resistance: int
    determination: int
    skill_speed: int
    spell_speed: int
    haste: int
    morale: int
    enmity: int
    enmity_reduction: int
    careful_desynthesis: int
    e_x_p_bonus: int
    regen: int
    refresh: int
    movement_speed: int
    spikes: int
    slow_resistance: int
    petrification_resistance: int
    paralysis_resistance: int
    silence_resistance: int
    blind_resistance: int
    poison_resistance: int
    stun_resistance: int
    sleep_resistance: int
    bind_resistance: int
    heavy_resistance: int
    doom_resistance: int
    reduced_durability_loss: int
    increased_spiritbond_gain: int
    craftsmanship: int
    control: int
    gathering: int
    perception: int

