import pandas as pd
import numpy as np

from main import df_all, df_im, df_dmg, df_hva, df_stam, df_thes, df_archief, df_agents

df_dmg_unique = df_dmg.sort_values('timestamp').groupby('URI').tail(1)
df_hva_unique = df_hva.sort_values('timestamp').groupby('URI').tail(1)
df_stam_unique = df_stam.sort_values('timestamp').groupby('URI').tail(1)
df_im_unique = df_im.sort_values('timestamp').groupby('URI').tail(1)
df_archief_unique = df_archief.sort_values('timestamp').groupby('URI').tail(1)


def reg_status():
    ##uri
    stam_uri_cnt = df_stam_unique.URI.replace("",np.nan).count()
    dmg_uri_cnt = df_dmg_unique.URI.replace("",np.nan).count()
    hva_uri_cnt = df_hva_unique.URI.replace("",np.nan).count()
    im_uri_cnt = df_im_unique.URI.replace("",np.nan).count()
    archief_uri_cnt = df_archief_unique.URI.replace("",np.nan).count()

    #owner
    stam_owner_cnt = df_stam_unique.owner.replace("",np.nan).count() / stam_uri_cnt * 100
    dmg_owner_cnt = df_dmg_unique.owner.replace("",np.nan).count() / dmg_uri_cnt * 100
    hva_owner_cnt = df_hva_unique.owner.replace("",np.nan).count() / hva_uri_cnt * 100
    im_owner_cnt = df_im_unique.owner.replace("",np.nan).count() / im_uri_cnt * 100
    archief_owner_cnt = df_archief_unique.owner.replace("",np.nan).count() / archief_uri_cnt * 100

    #title
    stam_title_cnt = df_stam_unique.title.replace("",np.nan).count() / stam_uri_cnt * 100
    dmg_title_cnt = df_dmg_unique.title.replace("",np.nan).count() / dmg_uri_cnt * 100
    hva_title_cnt = df_hva_unique.title.replace("",np.nan).count() / hva_uri_cnt * 100
    im_title_cnt = df_im_unique.title.replace("",np.nan).count() / im_uri_cnt * 100
    archief_title_cnt = df_archief_unique.title.replace("",np.nan).count() / archief_uri_cnt * 100

    #objectnaam
    stam_objname_cnt = df_stam_unique.object_name.replace("",np.nan).count() / stam_uri_cnt * 100
    dmg_objname_cnt = df_dmg_unique.object_name.replace("",np.nan).count() / dmg_uri_cnt * 100
    hva_objname_cnt = df_hva_unique.object_name.replace("",np.nan).count() / hva_uri_cnt * 100
    im_objname_cnt = df_im_unique.object_name.replace("",np.nan).count() / im_uri_cnt * 100
    archief_objname_cnt = df_archief_unique.object_name.replace("",np.nan).count() / archief_uri_cnt * 100

    #vervaardiger
    stam_creator_cnt = df_stam_unique.creator.replace("",np.nan).count() / stam_uri_cnt * 100
    dmg_creator_cnt = df_dmg_unique.creator.replace("",np.nan).count() / dmg_uri_cnt * 100
    hva_creator_cnt = df_hva_unique.creator.replace("",np.nan).count() / hva_uri_cnt * 100
    im_creator_cnt = df_im_unique.creator.replace("",np.nan).count() / im_uri_cnt * 100
    archief_creator_cnt = df_archief_unique.creator.replace("",np.nan).count() / archief_uri_cnt * 100

    #vervaardiger.rol
    stam_creator_role_cnt = df_stam_unique.creator_role.replace("",np.nan).count() / stam_uri_cnt * 100
    dmg_creator_role_cnt = df_dmg_unique.creator_role.replace("",np.nan).count() / dmg_uri_cnt * 100
    hva_creator_role_cnt = df_hva_unique.creator_role.replace("",np.nan).count() / hva_uri_cnt * 100
    im_creator_role_cnt = df_im_unique.creator_role.replace("",np.nan).count() / im_uri_cnt * 100
    archief_creator_role_cnt = df_archief_unique.creator_role.replace("",np.nan).count() / archief_uri_cnt * 100

    #vervaardiging.plaats
    stam_creator_place_cnt = df_stam_unique.creation_place.replace("",np.nan).count() / stam_uri_cnt * 100
    dmg_creator_place_cnt = df_dmg_unique.creation_place.replace("",np.nan).count() / dmg_uri_cnt * 100
    hva_creator_place_cnt = df_hva_unique.creation_place.replace("",np.nan).count() / hva_uri_cnt * 100
    im_creator_place_cnt = df_im_unique.creation_place.replace("",np.nan).count() / im_uri_cnt * 100
    archief_creator_place_cnt = df_archief_unique.creation_place.replace("",np.nan).count() / archief_uri_cnt * 100

    #vervaardiging.datum
    stam_creator_date_cnt = df_stam_unique.creation_date.replace("",np.nan).count() / stam_uri_cnt * 100
    dmg_creator_date_cnt = df_dmg_unique.creation_date.replace("",np.nan).count() / dmg_uri_cnt * 100
    hva_creator_date_cnt = df_hva_unique.creation_date.replace("",np.nan).count() / hva_uri_cnt * 100
    im_creator_date_cnt = df_im_unique.creation_date.replace("",np.nan).count() / im_uri_cnt * 100
    archief_creator_date_cnt = df_archief_unique.creation_date.replace("",np.nan).count() / archief_uri_cnt * 100

    cnt_all = pd.DataFrame({"STAM": [stam_owner_cnt, stam_title_cnt,
                                     stam_objname_cnt, stam_creator_cnt, stam_creator_place_cnt, stam_creator_role_cnt, stam_creator_date_cnt],
                            "DMG": [dmg_owner_cnt, dmg_title_cnt, dmg_objname_cnt, dmg_creator_cnt, dmg_creator_place_cnt, dmg_creator_role_cnt, dmg_creator_date_cnt],
                            "HVA": [hva_owner_cnt, hva_title_cnt, hva_objname_cnt, hva_creator_cnt, hva_creator_place_cnt, hva_creator_role_cnt, hva_creator_date_cnt],
                            "IM": [im_owner_cnt, im_title_cnt, im_objname_cnt, im_creator_cnt, im_creator_place_cnt, im_creator_role_cnt, im_creator_date_cnt],
                            "ARCHIEF": [archief_owner_cnt, archief_title_cnt, archief_objname_cnt, archief_creator_cnt, archief_creator_place_cnt, archief_creator_role_cnt, archief_creator_date_cnt]},
                           index=["eigenaar", "titel", "objectnaam", "vervaardiger", "plaats_van_vervaardiging", "vervaardiger_rol", "vervaardiging_datum"])
    return cnt_all


