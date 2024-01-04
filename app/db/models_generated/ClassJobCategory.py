from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class ClassJobCategory(SQLModel, table=True):
    __tablename__ = "class_job_category"
    __table_args__ = {'extend_existing': True}
    __allow_unmapped__ = True
    id: int = Field(default=None, primary_key=True)
    name: str
    a_d_v: bool
    g_l_a: bool
    p_g_l: bool
    m_r_d: bool
    l_n_c: bool
    a_r_c: bool
    c_n_j: bool
    t_h_m: bool
    c_r_p: bool
    b_s_m: bool
    a_r_m: bool
    g_s_m: bool
    l_t_w: bool
    w_v_r: bool
    a_l_c: bool
    c_u_l: bool
    m_i_n: bool
    b_t_n: bool
    f_s_h: bool
    p_l_d: bool
    m_n_k: bool
    w_a_r: bool
    d_r_g: bool
    b_r_d: bool
    w_h_m: bool
    b_l_m: bool
    a_c_n: bool
    s_m_n: bool
    s_c_h: bool
    r_o_g: bool
    n_i_n: bool
    m_c_h: bool
    d_r_k: bool
    a_s_t: bool
    s_a_m: bool
    r_d_m: bool
    b_l_u: bool
    g_n_b: bool
    d_n_c: bool
    r_p_r: bool
    s_g_e: bool

