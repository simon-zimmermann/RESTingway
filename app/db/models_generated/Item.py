from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from db.models_generated.ItemLevel import ItemLevel
    from db.models_generated.ItemUICategory import ItemUICategory
    from db.models_generated.ItemSearchCategory import ItemSearchCategory
    from db.models_generated.EquipSlotCategory import EquipSlotCategory
    from db.models_generated.ItemSortCategory import ItemSortCategory
    from db.models_generated.ItemAction import ItemAction
    from db.models_generated.ClassJob import ClassJob
    from db.models_generated.ItemRepairResource import ItemRepairResource
    from db.models_generated.ClassJobCategory import ClassJobCategory
    from db.models_generated.GrandCompany import GrandCompany
    from db.models_generated.ItemSeries import ItemSeries
    from db.models_generated.BaseParam import BaseParam
    from db.models_generated.ItemSpecialBonus import ItemSpecialBonus


class Item(SQLModel, table=True):
    __tablename__ = "item"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    singular: str
    adjective: int
    plural: str
    possessive_pronoun: int
    starts_with_vowel: int
    pronoun: int
    article: int
    description: str
    name: str
    icon: str
    level_item_id: Optional[int] = Field(default=None, foreign_key="item_level.id")
    level_item: Optional["ItemLevel"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.level_item_id]"})
    rarity: int
    filter_group: int
    additional_data: int
    item_u_i_category_id: Optional[int] = Field(default=None, foreign_key="item_u_i_category.id")
    item_u_i_category: Optional["ItemUICategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.item_u_i_category_id]"})
    item_search_category_id: Optional[int] = Field(default=None, foreign_key="item_search_category.id")
    item_search_category: Optional["ItemSearchCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.item_search_category_id]"})
    equip_slot_category_id: Optional[int] = Field(default=None, foreign_key="equip_slot_category.id")
    equip_slot_category: Optional["EquipSlotCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.equip_slot_category_id]"})
    item_sort_category_id: Optional[int] = Field(default=None, foreign_key="item_sort_category.id")
    item_sort_category: Optional["ItemSortCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.item_sort_category_id]"})
    stack_size: int
    is_unique: bool
    is_untradable: bool
    is_indisposable: bool
    lot: bool
    price_mid: int
    price_low: int
    can_be_hq: bool
    is_dyeable: bool
    is_crest_worthy: bool
    item_action_id: Optional[int] = Field(default=None, foreign_key="item_action.id")
    item_action: Optional["ItemAction"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.item_action_id]"})
    cast_times: int
    cooldowns: int
    class_job_repair_id: Optional[int] = Field(default=None, foreign_key="class_job.id")
    class_job_repair: Optional["ClassJob"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.class_job_repair_id]"})
    item_repair_id: Optional[int] = Field(default=None, foreign_key="item_repair_resource.id")
    item_repair: Optional["ItemRepairResource"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.item_repair_id]"})
    item_glamour_id: Optional[int] = Field(default=None, foreign_key="item.id")
    item_glamour: Optional["Item"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.item_glamour_id]"})
    desynth: int
    is_collectable: bool
    always_collectable: bool
    aetherial_reduce: int
    level_equip: int
    equip_restriction: int
    class_job_category_id: Optional[int] = Field(default=None, foreign_key="class_job_category.id")
    class_job_category: Optional["ClassJobCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.class_job_category_id]"})
    grand_company_id: Optional[int] = Field(default=None, foreign_key="grand_company.id")
    grand_company: Optional["GrandCompany"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.grand_company_id]"})
    item_series_id: Optional[int] = Field(default=None, foreign_key="item_series.id")
    item_series: Optional["ItemSeries"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.item_series_id]"})
    base_param_modifier: int
    model_main: str
    model_sub: str
    class_job_use_id: Optional[int] = Field(default=None, foreign_key="class_job.id")
    class_job_use: Optional["ClassJob"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.class_job_use_id]"})
    damage_phys: int
    damage_mag: int
    delayms: int
    block_rate: int
    block: int
    defense_phys: int
    defense_mag: int
    base_param0_id: Optional[int] = Field(default=None, foreign_key="base_param.id")
    base_param0: Optional["BaseParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.base_param0_id]"})
    base_param_value0: int
    base_param1_id: Optional[int] = Field(default=None, foreign_key="base_param.id")
    base_param1: Optional["BaseParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.base_param1_id]"})
    base_param_value1: int
    base_param2_id: Optional[int] = Field(default=None, foreign_key="base_param.id")
    base_param2: Optional["BaseParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.base_param2_id]"})
    base_param_value2: int
    base_param3_id: Optional[int] = Field(default=None, foreign_key="base_param.id")
    base_param3: Optional["BaseParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.base_param3_id]"})
    base_param_value3: int
    base_param4_id: Optional[int] = Field(default=None, foreign_key="base_param.id")
    base_param4: Optional["BaseParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.base_param4_id]"})
    base_param_value4: int
    base_param5_id: Optional[int] = Field(default=None, foreign_key="base_param.id")
    base_param5: Optional["BaseParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.base_param5_id]"})
    base_param_value5: int
    item_special_bonus_id: Optional[int] = Field(default=None, foreign_key="item_special_bonus.id")
    item_special_bonus: Optional["ItemSpecialBonus"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.item_special_bonus_id]"})
    item_special_bonus_param: int
    base_param_special0_id: Optional[int] = Field(default=None, foreign_key="base_param.id")
    base_param_special0: Optional["BaseParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.base_param_special0_id]"})
    base_param_value_special0: int
    base_param_special1_id: Optional[int] = Field(default=None, foreign_key="base_param.id")
    base_param_special1: Optional["BaseParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.base_param_special1_id]"})
    base_param_value_special1: int
    base_param_special2_id: Optional[int] = Field(default=None, foreign_key="base_param.id")
    base_param_special2: Optional["BaseParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.base_param_special2_id]"})
    base_param_value_special2: int
    base_param_special3_id: Optional[int] = Field(default=None, foreign_key="base_param.id")
    base_param_special3: Optional["BaseParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.base_param_special3_id]"})
    base_param_value_special3: int
    base_param_special4_id: Optional[int] = Field(default=None, foreign_key="base_param.id")
    base_param_special4: Optional["BaseParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.base_param_special4_id]"})
    base_param_value_special4: int
    base_param_special5_id: Optional[int] = Field(default=None, foreign_key="base_param.id")
    base_param_special5: Optional["BaseParam"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Item.base_param_special5_id]"})
    base_param_value_special5: int
    materialize_type: int
    materia_slot_count: int
    is_advanced_melding_permitted: bool
    is_pv_p: bool
    sub_stat_category: int
    is_glamourous: bool

