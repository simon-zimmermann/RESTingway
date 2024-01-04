from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class MountCustomize(SQLModel, table=True):
    __tablename__ = "mount_customize"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    hyur_midlander_male_scale: int
    hyur_midlander_female_scale: int
    hyur_highlander_male_scale: int
    hyur_highlander_female_scale: int
    elezen_male_scale: int
    elezen_female_scale: int
    lala_male_scale: int
    lala_female_scale: int
    miqo_male_scale: int
    miqo_female_scale: int
    roe_male_scale: int
    roe_female_scale: int
    au_ra_male_scale: int
    au_ra_female_scale: int
    hrothgar_male_scale: int
    viera_male_scale: int
    viera_female_scale: int
    hyur_midlander_male_camera_height: int
    hyur_midlander_female_camera_height: int
    hyur_highlander_male_camera_height: int
    hyur_highlander_female_camera_height: int
    elezen_male_camera_height: int
    elezen_female_camera_height: int
    lala_male_camera_height: int
    lala_female_camera_height: int
    miqo_male_camera_height: int
    miqo_female_camera_height: int
    roe_male_camera_height: int
    roe_female_camera_height: int
    au_ra_male_camera_height: int
    au_ra_female_camera_height: int
    hrothgar_male_camera_height: int
    viera_male_camera_height: int
    viera_female_camera_height: int

