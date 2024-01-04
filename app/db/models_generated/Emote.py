from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.storingway.models_generated.ActionTimeline import ActionTimeline
    from app.storingway.models_generated.EmoteCategory import EmoteCategory
    from app.storingway.models_generated.EmoteMode import EmoteMode
    from app.storingway.models_generated.TextCommand import TextCommand
    from app.storingway.models_generated.LogMessage import LogMessage


class Emote(SQLModel, table=True):
    __tablename__ = "emote"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    action_timeline0_id: Optional[int] = Field(default=None, foreign_key="action_timeline.id")
    action_timeline0: Optional["ActionTimeline"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Emote.action_timeline0_id]"})
    action_timeline1_id: Optional[int] = Field(default=None, foreign_key="action_timeline.id")
    action_timeline1: Optional["ActionTimeline"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Emote.action_timeline1_id]"})
    action_timeline2_id: Optional[int] = Field(default=None, foreign_key="action_timeline.id")
    action_timeline2: Optional["ActionTimeline"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Emote.action_timeline2_id]"})
    action_timeline3_id: Optional[int] = Field(default=None, foreign_key="action_timeline.id")
    action_timeline3: Optional["ActionTimeline"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Emote.action_timeline3_id]"})
    action_timeline4_id: Optional[int] = Field(default=None, foreign_key="action_timeline.id")
    action_timeline4: Optional["ActionTimeline"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Emote.action_timeline4_id]"})
    action_timeline5_id: Optional[int] = Field(default=None, foreign_key="action_timeline.id")
    action_timeline5: Optional["ActionTimeline"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Emote.action_timeline5_id]"})
    action_timeline6_id: Optional[int] = Field(default=None, foreign_key="action_timeline.id")
    action_timeline6: Optional["ActionTimeline"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Emote.action_timeline6_id]"})
    emote_category_id: Optional[int] = Field(default=None, foreign_key="emote_category.id")
    emote_category: Optional["EmoteCategory"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Emote.emote_category_id]"})
    emote_mode_id: Optional[int] = Field(default=None, foreign_key="emote_mode.id")
    emote_mode: Optional["EmoteMode"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Emote.emote_mode_id]"})
    has_cancel_emote: bool
    draws_weapon: bool
    order: int
    text_command_id: Optional[int] = Field(default=None, foreign_key="text_command.id")
    text_command: Optional["TextCommand"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Emote.text_command_id]"})
    icon: str
    log_message_targeted_id: Optional[int] = Field(default=None, foreign_key="log_message.id")
    log_message_targeted: Optional["LogMessage"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Emote.log_message_targeted_id]"})
    log_message_untargeted_id: Optional[int] = Field(default=None, foreign_key="log_message.id")
    log_message_untargeted: Optional["LogMessage"] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Emote.log_message_untargeted_id]"})
    unlock_link: int

