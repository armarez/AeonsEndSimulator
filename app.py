import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Dossier dans lequel se trouve app.py
DOSSIER_APPLICATION = Path(__file__).parent

# Sous-dossier contenant les images
DOSSIER_IMAGES = DOSSIER_APPLICATION / "images"

# Association entre les cartes et leurs fichiers image
IMAGES_CARTES = {
    "Cinder": DOSSIER_IMAGES / "cinder.jpg",
    "Mazra's Studies": DOSSIER_IMAGES / "mazras_studies.jpg",
    "Mazra's Arc": DOSSIER_IMAGES / "mazras_arc.jpg",
    "Mazra's Wisdom": DOSSIER_IMAGES / "mazras_wisdom.jpg",
    "Mazra's Gift": DOSSIER_IMAGES / "mazras_gift.jpg",
    "Mazra's Inferno": DOSSIER_IMAGES / "mazras_inferno.jpg",
    "Eternal Ember": DOSSIER_IMAGES / "eternal_ember.jpg",
    "Obsidian Shard": DOSSIER_IMAGES / "obsidian_shard.jpg",
    "Change Form": DOSSIER_IMAGES / "Change_Form.jpg",
    "Melded Radite": DOSSIER_IMAGES / "Melded_Radite.jpg",
    "Tourmaline Shard": DOSSIER_IMAGES / "tourmaline_shard.jpg",
    "Lurking Sionite": DOSSIER_IMAGES / "lurking_sionite.jpg",
    "Jade": DOSSIER_IMAGES / "jade.jpg",
    "Diamond Cluster": DOSSIER_IMAGES / "diamond_cluster.jpg",
    "Bottled Vortex": DOSSIER_IMAGES / "bottled_vortex.jpg",
    "Lava Tendril": DOSSIER_IMAGES / "lava_tendril.jpg",
    "Garnet Shard": DOSSIER_IMAGES / "garnet_shard.jpg",
    "Quartz Shard": DOSSIER_IMAGES / "quartz_shard.jpg",
    "Moonstone Shard": DOSSIER_IMAGES / "moonstone_shard.jpg",
    "Amethyst Shard": DOSSIER_IMAGES / "amethyst_shard.jpg",
    # Cartes de depart
    "Crystal": DOSSIER_IMAGES / "crystal.jpg",
    "Spark": DOSSIER_IMAGES / "spark.jpg",
    "Emerald Shard": DOSSIER_IMAGES / "emerald_shard.jpg",
    "Buried Light": DOSSIER_IMAGES / "buried_light.jpg",
    "Flare": DOSSIER_IMAGES / "flare.jpg",

    # Gemmes du marche
    "Ambre de V'risbois": DOSSIER_IMAGES / "ambre_vrisbois.jpg",
    "Pointe de vide": DOSSIER_IMAGES / "pointe_de_vide.jpg",
    "Clouded Sapphire": DOSSIER_IMAGES / "clouded_sapphire.jpg",
    "Invoquine": DOSSIER_IMAGES / "invoquine.jpg",
    "Voltecorce": DOSSIER_IMAGES / "voltecorce.jpg",
    "Voltécorce": DOSSIER_IMAGES / "voltecorce.jpg",

    # Reliques du marche
    "Focusing Orb": DOSSIER_IMAGES / "focusing_orb.jpg",
    "Etoile miniature": DOSSIER_IMAGES / "etoile_miniature.jpg",
    "Étoile miniature": DOSSIER_IMAGES / "etoile_miniature.jpg",
    "Puits d'Energie": DOSSIER_IMAGES / "puits_energie.jpg",
    "Puits d'Énergie": DOSSIER_IMAGES / "puits_energie.jpg",
    "Talisman de mage": DOSSIER_IMAGES / "talisman_de_mage.jpg",
    "Cube sans fond": DOSSIER_IMAGES / "cube_sans_fond.jpg",
    "Transmogrifieur": DOSSIER_IMAGES / "transmogrifieur.jpg",
    "Filaments d'ame": DOSSIER_IMAGES / "filaments_ame.jpg",
    "Filaments d'âme": DOSSIER_IMAGES / "filaments_ame.jpg",

    # Sorts du marche
    "Force colossale": DOSSIER_IMAGES / "force_colossale.jpg",
    "Invoque-debris": DOSSIER_IMAGES / "invoque_debris.jpg",
    "Invoque-débris": DOSSIER_IMAGES / "invoque_debris.jpg",
    "Ombre Devorante": DOSSIER_IMAGES / "ombre_devorante.jpg",
    "Ombre Dévorante": DOSSIER_IMAGES / "ombre_devorante.jpg",
    "Faux de desintegration": DOSSIER_IMAGES / "faux_desintegration.jpg",
    "Faux de désintégration": DOSSIER_IMAGES / "faux_desintegration.jpg",
}


def image_carte(nom_carte):
    """Retourne l'image si le fichier existe, sinon None."""
    chemin = IMAGES_CARTES.get(nom_carte)
    if chemin is not None and chemin.exists():
        return chemin
    return None

st.set_page_config(
    page_title="Simulateur Aeon's End",
    page_icon="⚡",
    layout="wide"
)

# Interface compacte et bouton principal rouge
st.markdown(
    """
    <style>
        /* Réduire les marges générales */
        /* Interface placée au plus haut */
        header[data-testid="stHeader"] {
            display: none;
        }
        div[data-testid="stToolbar"] {
            display: none;
        }
        #MainMenu {
            visibility: hidden;
        }
        .block-container {
            max-width: 1600px;
            padding-top: 0.05rem;
            padding-bottom: 0.35rem;
            padding-left: 0.55rem;
            padding-right: 0.55rem;
        }

        /* Sélecteur du mage compact */
        div[data-testid="stSelectbox"] {
            margin-top: 0 !important;
            margin-bottom: 0.05rem !important;
        }
        div[data-testid="stSelectbox"] label {
            min-height: 1.2rem !important;
            margin-bottom: 0.1rem !important;
        }

        /* Titres plus compacts */
        h1 { font-size: 1.75rem !important; margin-bottom: 0.25rem !important; }
        h2 { font-size: 1.35rem !important; margin-top: 0.35rem !important; }
        h3 { font-size: 1.10rem !important; margin-top: 0.25rem !important; }

        /* Réduire l'espace entre les blocs */
        div[data-testid="stVerticalBlock"] { gap: 0.22rem; }
        div[data-testid="stHorizontalBlock"] { gap: 0.35rem; }
        hr { margin: 0.25rem 0 !important; }

        /* Cartes et messages plus compacts */
        div[data-testid="stAlert"] {
            padding: 0.30rem 0.48rem;
            min-height: 0;
        }
        div[data-testid="stMetric"] {
            background: #151b24;
            border: 1px solid #2b3442;
            border-radius: 7px;
            padding: 0.22rem 0.48rem;
        }

        /* Bouton principal Terminer le tour */
        button[kind="primary"] {
            background: #ff4b55 !important;
            border-color: #ff4b55 !important;
            color: white !important;
            min-height: 2.05rem;
            font-weight: 700 !important;
            border-radius: 7px !important;
        }
        button[kind="primary"]:hover {
            background: #e63946 !important;
            border-color: #e63946 !important;
        }

        /* Boutons secondaires plus courts */
        button[kind="secondary"] {
            min-height: 1.85rem;
            padding-top: 0.08rem !important;
            padding-bottom: 0.08rem !important;
        }

        /* Images de cartes sans espace superflu */
        div[data-testid="stImage"] { margin-bottom: 0.1rem; }
    

        /* Marché plus compact */
        div[data-testid="stTabs"] div[data-testid="stImage"] img {
            max-height: 245px;
            width: auto !important;
            object-fit: contain;
            border-radius: 8px;
        }

        div[data-testid="stTabs"] p {
            margin-bottom: 0.15rem;
            line-height: 1.15;
        }

        div[data-testid="stTabs"] button {
            min-height: 2rem;
            padding-top: 0.2rem !important;
            padding-bottom: 0.2rem !important;
        }

    

        /* Marché : images centrées, sans texte sous les cartes */
        div[data-testid="stTabs"] div[data-testid="stImage"] {
            display: flex;
            justify-content: center;
        }
        div[data-testid="stTabs"] div[data-testid="stColumn"] {
            text-align: center;
        }

    

        /* Deck compact placé en bas */
        .deck-card-compact {
            background: #133c2b;
            color: #65f59a;
            border: 1px solid #24553f;
            border-radius: 7px;
            padding: 0.32rem 0.48rem;
            margin: 0.12rem 0;
            min-height: 1.9rem;
            font-size: 0.86rem;
            line-height: 1.15;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .deck-position {
            color: #a5f3c1;
            font-weight: 700;
        }

        /* Mode très compact */
        html, body, [class*="css"] { font-size: 14px; }
        p, label, .stCaption { line-height: 1.15 !important; }
        div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
            min-height: 2.05rem !important;
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }
        div[data-testid="stMetric"] label { font-size: 0.82rem !important; }
        div[data-testid="stMetricValue"] { font-size: 1.65rem !important; }
        div[data-testid="stProgress"] { margin-top: -0.15rem; margin-bottom: -0.10rem; }
        div[data-testid="stAlert"] p { font-size: 0.86rem !important; margin: 0 !important; }
        div[data-testid="stButton"] { margin: 0 !important; }
        button { font-size: 0.88rem !important; }
        h2 { margin-bottom: 0.10rem !important; }
        div[data-testid="stCaptionContainer"] { margin-top: -0.08rem; }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# DONNÉES DES CARTES
# --------------------------------------------------

CARTES = {
    "Crystal": {
        "type": "gemme",
        "aether": 1
    },
    "Emerald Shard": {
        "type": "gemme",
        "aether": 1
    },
    "Spark": {
        "type": "sort",
        "aether": 0
    },
    "Buried Light": {
        "type": "sort",
        "aether": 0
    },
    "Flare": {
        "type": "sort",
        "aether": 0
    }
}

# --------------------------------------------------
# MARCHÉ
# --------------------------------------------------

MARCHE = {
    "Gemmes": [
        {"nom": "Lurking Sionite", "cout": 3, "extension": "The New Age", "role": "Synergie allié"},
        {"nom": "Diamond Cluster", "cout": 4, "extension": "Core Set", "role": "Combo gemme"},
        {"nom": "Jade", "cout": 2, "extension": "Core Set", "role": "Économie"},
        {"nom": "Ambre de V'risbois", "cout": 3, "extension": "Core Set", "role": "Rush Gemme"},
        {"nom": "Pointe de vide", "cout": 3, "extension": "Secrets Enfouis", "role": "Charge"},
        {"nom": "Clouded Sapphire", "cout": 6, "extension": "Core Set", "role": "Charge"},
        {"nom": "Invoquine", "cout": 3, "extension": "Secrets Enfouis", "role": "Spam Gemme"},
        {"nom": "Voltécorce", "cout": 3, "extension": "Secrets Enfouis", "role": "Charge"},
    ],
    "Reliques": [
        {"nom": "Bottled Vortex", "cout": 3, "extension": "Core Set", "role": "Destruction"},
        {"nom": "Focusing Orb", "cout": 4, "extension": "Core Set", "role": "Brèche"},
        {"nom": "Étoile miniature", "cout": 7, "extension": "Secrets Enfouis", "role": "3 Charges"},
        {"nom": "Puits d'Énergie", "cout": 7, "extension": "Nouvelle Ère", "role": "Soin"},
        {"nom": "Talisman de mage", "cout": 6, "extension": "Core Set", "role": "Charge"},
        {"nom": "Cube sans fond", "cout": 4, "extension": "Secrets Enfouis", "role": "Spam Carte"},
        {"nom": "Transmogrifieur", "cout": 4, "extension": "Profondeurs", "role": "Recyclage"},
        {"nom": "Filaments d'âme", "cout": 5, "extension": "Secrets Enfouis", "role": "Charge"},
    ],
    "Sorts": [
        {"nom": "Lava Tendril", "cout": 4, "extension": "Core Set", "role": "Dégâts persistants"},
        {"nom": "Force colossale", "cout": 5, "extension": "Secrets Enfouis", "role": "Silence"},
        {"nom": "Invoque-débris", "cout": 5, "extension": "Vieux Souvenirs", "role": "Carte 0 / Kadir-Lash"},
        {"nom": "Ombre Dévorante", "cout": 6, "extension": "Profondeurs", "role": "Optimisation"},
        {"nom": "Faux de désintégration", "cout": 7, "extension": "Profondeurs", "role": "Burst"},
    ],
}

# Ces cartes peuvent être achetées et circuler dans le deck. Leur effet détaillé
# sera intégré progressivement. Tant que l'effet n'est pas intégré, elles sont
# visibles en main mais ne proposent pas d'action incorrecte.
for categorie, cartes_marche in MARCHE.items():
    type_carte = {
        "Gemmes": "gemme_marche",
        "Reliques": "relique_marche",
        "Sorts": "sort_marche",
    }[categorie]

    for carte_marche in cartes_marche:
        CARTES[carte_marche["nom"]] = {
            "type": type_carte,
            "aether": 0,
            "effet_integre": False,
        }

# Lurking Sionite : +2 Æthers, ou +3 si une Lurking Sionite est présente
# dans la défausse d'un allié. En solo, la propre défausse est vérifiée.
CARTES["Lurking Sionite"] = {
    "type": "lurking_sionite",
    "aether": 2,
    "effet_integre": True,
}

# Jade : gagne 2 Æthers.
CARTES["Jade"] = {
    "type": "gemme",
    "aether": 2,
    "effet_integre": True,
}

# Diamond Cluster : gagne 2 Æthers ; le deuxième joué ce tour gagne +2 Æthers.
CARTES["Diamond Cluster"] = {
    "type": "diamond_cluster",
    "aether": 2,
    "effet_integre": True,
}

# Bottled Vortex : se détruit, détruit jusqu'à deux cartes de la main
# et/ou de la défausse, puis pioche une carte.
CARTES["Bottled Vortex"] = {
    "type": "bottled_vortex",
    "aether": 0,
    "effet_integre": True,
}

# Lava Tendril : 1 dégât à la fin de la phase d'incantation tant qu'il est
# préparé, puis 3 dégâts lorsqu'il est lancé.
CARTES["Lava Tendril"] = {
    "type": "sort",
    "aether": 0,
    "degats": 3,
    "effet_integre": True,
}

# Ambre de V'risbois est deja entierement geree :
# elle produit 2 Aethers lorsqu'elle est jouee.
CARTES["Ambre de V'risbois"] = {
    "type": "gemme",
    "aether": 2,
    "effet_integre": True,
}

# Clouded Sapphire est une gemme jouable.
# Son effet economique est integre : +3 Aethers.
# L'effet de charge d'un allie sera ajoute avec le mode multijoueur.
CARTES["Clouded Sapphire"] = {
    "type": "gemme",
    "aether": 3,
    "effet_integre": True,
}


# Invoquine produit simplement 2 Æthers dans la version actuelle.
CARTES["Invoquine"] = {
    "type": "gemme",
    "aether": 2,
    "effet_integre": True,
}

# Pointe de vide produit 2 Æthers et propose un effet optionnel :
# défausser une autre carte de la main pour gagner 1 charge.
CARTES["Pointe de vide"] = {
    "type": "pointe_de_vide",
    "aether": 2,
    "effet_integre": True,
}


# Voltécorce possède deux choix au moment où elle est jouée.
CARTES["Voltécorce"] = {
    "type": "voltecorce",
    "aether": 2,
    "effet_integre": True,
}

# Ombre Dévorante est un sort jouable avec un effet tant qu'il reste préparé.
CARTES["Ombre Dévorante"] = {
    "type": "sort",
    "aether": 0,
    "degats": 3,
    "effet_integre": True,
}


# Faux de désintégration : 8 dégâts, -1 PV, puis transmise à un autre joueur.
CARTES["Faux de désintégration"] = {
    "type": "sort",
    "aether": 0,
    "degats": 8,
    "effet_integre": True,
}


# Sorts offensifs intégrés.
CARTES["Force colossale"] = {
    "type": "sort",
    "aether": 0,
    "degats": 4,
    "effet_integre": True,
}

CARTES["Invoque-débris"] = {
    "type": "sort",
    "aether": 0,
    "degats": 4,
    "effet_integre": True,
}

RELIQUES_INTEGREES = {
    "Focusing Orb": "orbe_stabilisation",
    "Étoile miniature": "etoile_miniature",
    "Puits d'Énergie": "puits_energie",
    "Talisman de mage": "talisman_mage",
    "Cube sans fond": "cube_sans_fond",
    "Transmogrifieur": "transmogrifieur",
    "Filaments d'âme": "filaments_ame",
}
for nom_relique, type_relique in RELIQUES_INTEGREES.items():
    CARTES[nom_relique] = {"type": type_relique, "aether": 0, "effet_integre": True}

# Carte de départ d'Adelheim.
CARTES["Amethyst Shard"] = {
    "type": "gemme",
    "aether": 1,
    "effet_integre": True,
}

# Carte de départ de Jian.
# Produit 1 Æther normal et 1 Æther réservé à l'achat d'une gemme.
CARTES["Moonstone Shard"] = {
    "type": "moonstone_shard",
    "aether": 1,
    "aether_gemme": 1,
    "effet_integre": True,
}

# Carte de départ de Lash.
CARTES["Quartz Shard"] = {
    "type": "quartz_shard",
    "aether": 1,
    "effet_integre": True,
}

# Carte de départ de Mist.
# Dans cette version, le gain de 1 Æther est automatisé.
CARTES["Garnet Shard"] = {
    "type": "gemme",
    "aether": 1,
    "effet_integre": True,
}

# Carte de départ de Phaedraxa.
CARTES["Tourmaline Shard"] = {
    "type": "tourmaline_shard",
    "aether": 1,
    "effet_integre": True,
}

# Cartes de départ de Qu.
CARTES["Change Form"] = {
    "type": "change_form",
    "aether": 0,
    "effet_integre": True,
}
CARTES["Melded Radite"] = {
    "type": "melded_radite",
    "aether": 0,
    "effet_integre": True,
}

# Gemme de départ de Reeve.
CARTES["Obsidian Shard"] = {
    "type": "obsidian_shard",
    "aether": 1,
    "effet_integre": True,
}

# Sort de départ de Z'hana.
CARTES["Eternal Ember"] = {
    "type": "eternal_ember",
    "aether": 0,
    "degats": 1,
    "effet_integre": True,
}

# Cartes personnelles de Mazra.
CARTES["Mazra's Studies"] = {"type": "sort", "aether": 0, "degats": 1, "cout": 0, "effet_integre": True}
CARTES["Mazra's Arc"] = {"type": "sort", "aether": 0, "degats": 3, "cout": 3, "effet_integre": True}
CARTES["Mazra's Wisdom"] = {"type": "sort", "aether": 0, "degats": 2, "cout": 3, "effet_integre": True}
CARTES["Mazra's Gift"] = {"type": "sort", "aether": 0, "degats": 4, "cout": 6, "effet_integre": True}
CARTES["Mazra's Inferno"] = {"type": "sort", "aether": 0, "degats": 6, "cout": 6, "effet_integre": True}

# Carte de départ de Nym : au lancement, choisir 1 dégât ou +2 Æthers.
CARTES["Cinder"] = {
    "type": "cinder",
    "aether": 0,
    "degats": 1,
    "effet_integre": True,
}

# --------------------------------------------------
# BRECHES DE KADIR
# --------------------------------------------------

BRECHES_KADIR = [
    {
        "numero": "I",
        "ouverte": True,
        "etape": 0,
        "cout_focus": 0,
        "couts_ouverture": [0],
        "bonus_degats": 0,
    },
    {
        "numero": "II",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 2,
        "couts_ouverture": [3, 2],
        "bonus_degats": 0,
    },
    {
        "numero": "III",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 3,
        "couts_ouverture": [7, 5, 3],
        "bonus_degats": 1,
    },
    {
        "numero": "IV",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 4,
        "couts_ouverture": [7, 4],
        "bonus_degats": 1,
    },
]


# Brèches de départ d'Adelheim.
BRECHES_ADELHEIM = [
    {
        "numero": "I",
        "ouverte": True,
        "etape": 0,
        "cout_focus": 0,
        "couts_ouverture": [0],
        "bonus_degats": 0,
    },
    {
        "numero": "II",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 2,
        "couts_ouverture": [3, 2],
        "bonus_degats": 0,
    },
    {
        "numero": "III",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 3,
        "couts_ouverture": [9, 7, 5, 3],
        "bonus_degats": 1,
    },
    {
        "numero": "IV",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 4,
        "couts_ouverture": [10, 7, 4],
        "bonus_degats": 1,
    },
]

# Brèches de Jian : I et II ouvertes, III et IV fermées.
BRECHES_JIAN = [
    {
        "numero": "I",
        "ouverte": True,
        "etape": 0,
        "cout_focus": 0,
        "couts_ouverture": [0],
        "bonus_degats": 0,
    },
    {
        "numero": "II",
        "ouverte": True,
        "etape": 0,
        "cout_focus": 0,
        "couts_ouverture": [0],
        "bonus_degats": 0,
    },
    {
        "numero": "III",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 3,
        "couts_ouverture": [9, 7, 5, 3],
        "bonus_degats": 1,
    },
    {
        "numero": "IV",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 4,
        "couts_ouverture": [10, 7, 4],
        "bonus_degats": 1,
    },
]

# Brèches de Lash : I ouverte, II/III/IV fermées.
BRECHES_LASH = [
    {
        "numero": "I",
        "ouverte": True,
        "etape": 0,
        "cout_focus": 0,
        "couts_ouverture": [0],
        "bonus_degats": 0,
    },
    {
        "numero": "II",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 2,
        "couts_ouverture": [3, 2],
        "bonus_degats": 0,
    },
    {
        "numero": "III",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 3,
        "couts_ouverture": [9, 7, 5, 3],
        "bonus_degats": 1,
    },
    {
        "numero": "IV",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 4,
        "couts_ouverture": [7, 4],
        "bonus_degats": 1,
    },
]

BRECHES_BRAMA = [
    {
        "numero": "I",
        "ouverte": True,
        "etape": 0,
        "cout_focus": 0,
        "couts_ouverture": [0],
        "bonus_degats": 0,
    },
    {
        "numero": "II",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 2,
        "couts_ouverture": [4, 3, 2],
        "bonus_degats": 0,
    },
    {
        "numero": "III",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 3,
        "couts_ouverture": [9, 7, 5, 3],
        "bonus_degats": 1,
    },
    {
        "numero": "IV",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 4,
        "couts_ouverture": [7, 4],
        "bonus_degats": 1,
    },
]

BRECHES_XAXOS = [
    {
        "numero": "I",
        "ouverte": True,
        "etape": 0,
        "cout_focus": 0,
        "couts_ouverture": [0],
        "bonus_degats": 0,
    },
    {
        "numero": "II",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 2,
        "couts_ouverture": [5, 4, 3, 2],
        "bonus_degats": 0,
    },
    {
        "numero": "III",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 3,
        "couts_ouverture": [9, 7, 5, 3],
        "bonus_degats": 1,
    },
    {
        "numero": "IV",
        "ouverte": False,
        "etape": 0,
        "cout_focus": 4,
        "couts_ouverture": [10, 7, 4],
        "bonus_degats": 1,
    },
]

# Brèches de Phaedraxa : uniquement II, III et IV.
BRECHES_QU = [
    {"numero": "I", "ouverte": True, "etape": 0, "cout_focus": 0, "couts_ouverture": [0], "bonus_degats": 0},
    {"numero": "II", "ouverte": False, "etape": 0, "cout_focus": 2, "couts_ouverture": [4, 3, 2], "bonus_degats": 0},
    {"numero": "III", "ouverte": False, "etape": 0, "cout_focus": 3, "couts_ouverture": [9, 7, 5, 3], "bonus_degats": 1},
    {"numero": "IV", "ouverte": False, "etape": 0, "cout_focus": 4, "couts_ouverture": [10, 7, 4], "bonus_degats": 1},
]

BRECHES_REEVE = [
    {"numero": "I", "ouverte": True, "etape": 0, "cout_focus": 0, "couts_ouverture": [0], "bonus_degats": 0},
    # Une focalisation fait tourner la brèche dans le sens horaire :
    # le coût situé à gauche devient le nouveau coût placé en haut.
    {"numero": "II", "ouverte": False, "etape": 0, "cout_focus": 2, "couts_ouverture": [3, 2, 5, 4], "bonus_degats": 0},
    {"numero": "III", "ouverte": False, "etape": 0, "cout_focus": 3, "couts_ouverture": [7, 5, 3, 9], "bonus_degats": 1},
    {"numero": "IV", "ouverte": False, "etape": 0, "cout_focus": 4, "couts_ouverture": [7, 4, 13, 10], "bonus_degats": 1},
]

BRECHES_ZHANA = [
    # Z'hana ne possède pas de brèche I.
    # Une focalisation tourne la brèche dans le sens horaire :
    # le coût situé à gauche devient le nouveau coût supérieur.
    {"numero": "II", "ouverte": False, "etape": 0, "cout_focus": 2, "couts_ouverture": [5, 4, 3, 2], "bonus_degats": 0},
    {"numero": "III", "ouverte": False, "etape": 0, "cout_focus": 3, "couts_ouverture": [7, 5, 3, 9], "bonus_degats": 1},
    {"numero": "IV", "ouverte": False, "etape": 0, "cout_focus": 4, "couts_ouverture": [4, 13, 10, 7], "bonus_degats": 1},
]

BRECHES_MAZRA = [
    {"numero": "I", "ouverte": True, "etape": 0, "cout_focus": 0, "couts_ouverture": [0], "bonus_degats": 0},
    {"numero": "II", "ouverte": False, "etape": 0, "cout_focus": 2, "couts_ouverture": [5, 4, 3, 2], "bonus_degats": 0},
    # Brèche de Recherche : Mazra gagne 1 charge quand un sort y est lancé.
    {"numero": "III", "ouverte": False, "etape": 0, "cout_focus": 3, "couts_ouverture": [7, 5, 3, 9], "bonus_degats": 0, "charge_sur_lancement": True},
    {"numero": "IV", "ouverte": False, "etape": 0, "cout_focus": 4, "couts_ouverture": [13, 10, 7, 4], "bonus_degats": 1},
]

BRECHES_NYM = [
    {"numero": "I", "ouverte": True, "etape": 0, "cout_focus": 0, "couts_ouverture": [0], "bonus_degats": 0},
    # Une focalisation tourne la brèche dans le sens horaire :
    # le coût situé à gauche devient le nouveau coût supérieur.
    {"numero": "II", "ouverte": False, "etape": 0, "cout_focus": 2, "couts_ouverture": [5, 4, 3, 2], "bonus_degats": 0},
    {"numero": "III", "ouverte": False, "etape": 0, "cout_focus": 3, "couts_ouverture": [7, 5, 3, 9], "bonus_degats": 1},
    {"numero": "IV", "ouverte": False, "etape": 0, "cout_focus": 4, "couts_ouverture": [10, 7, 4, 13], "bonus_degats": 1},
]

BRECHES_PHAEDRAXA = [
    {"numero": "II", "ouverte": True,  "etape": 0, "cout_focus": 0, "couts_ouverture": [0], "bonus_degats": 0},
    {"numero": "III", "ouverte": False, "etape": 0, "cout_focus": 3, "couts_ouverture": [7, 5, 3], "bonus_degats": 1},
    {"numero": "IV", "ouverte": False, "etape": 0, "cout_focus": 4, "couts_ouverture": [10, 7, 4], "bonus_degats": 1},
]

# --------------------------------------------------
# CONFIGURATION DES MAGES
# --------------------------------------------------

MAGES = {
    "Nym": {
        "main": ["Cinder", "Crystal", "Crystal", "Crystal", "Crystal"],
        "deck": ["Crystal", "Crystal", "Crystal", "Spark", "Spark"]
    },
    "Mazra": {
        "main": ["Crystal", "Crystal", "Crystal", "Crystal", "Mazra's Studies"],
        "deck": ["Crystal", "Crystal", "Crystal", "Crystal", "Mazra's Studies"]
    },
    "Z'hana": {
        "main": ["Eternal Ember", "Crystal", "Crystal", "Crystal", "Crystal"],
        "deck": ["Crystal", "Crystal", "Crystal", "Crystal", "Spark"]
    },
    "Reeve": {
        "main": ["Obsidian Shard", "Crystal", "Crystal", "Spark", "Spark"],
        "deck": ["Crystal", "Crystal", "Crystal", "Spark", "Spark"]
    },
    "Qu": {
        "main": ["Crystal", "Crystal", "Change Form", "Spark", "Spark"],
        "deck": ["Spark", "Spark", "Melded Radite", "Crystal", "Crystal"]
    },
    "Phaedraxa": {
        "main": ["Tourmaline Shard", "Crystal", "Crystal", "Crystal", "Spark"],
        "deck": ["Crystal", "Crystal", "Crystal", "Crystal", "Spark"]
    },
    "Mist": {
        "main": ["Garnet Shard", "Crystal", "Crystal", "Crystal", "Spark"],
        "deck": ["Crystal", "Crystal", "Crystal", "Spark", "Spark"]
    },
    "Lash": {
        "main": ["Quartz Shard", "Crystal", "Crystal", "Crystal", "Spark"],
        "deck": ["Crystal", "Crystal", "Crystal", "Spark", "Spark"]
    },
    "Jian": {
        "main": ["Moonstone Shard", "Crystal", "Crystal", "Spark", "Spark"],
        "deck": ["Crystal", "Crystal", "Crystal", "Spark", "Spark"]
    },
    "Adelheim": {
        "main": ["Amethyst Shard", "Crystal", "Crystal", "Spark", "Spark"],
        "deck": ["Crystal", "Crystal", "Crystal", "Crystal", "Crystal"]
    },
    "Kadir": {
        "main": [
            "Emerald Shard",
            "Crystal",
            "Crystal",
            "Crystal",
            "Spark"
        ],
        "deck": [
            "Crystal",
            "Crystal",
            "Crystal",
            "Spark",
            "Spark"
        ]
    },
    "Brama": {
        "main": [
            "Buried Light",
            "Crystal",
            "Crystal",
            "Crystal",
            "Crystal"
        ],
        "deck": [
            "Crystal",
            "Crystal",
            "Crystal",
            "Spark",
            "Spark"
        ]
    },
    "Xaxos": {
        "main": [
            "Flare",
            "Crystal",
            "Crystal",
            "Crystal",
            "Crystal"
        ],
        "deck": [
            "Crystal",
            "Crystal",
            "Crystal",
            "Crystal",
            "Spark"
        ]
    }
}

# --------------------------------------------------
# INITIALISATION DE LA PARTIE
# --------------------------------------------------

def initialiser_partie(nom_mage):
    st.session_state.mage_actuel = nom_mage
    st.session_state.main = MAGES[nom_mage]["main"].copy()
    st.session_state.deck = MAGES[nom_mage]["deck"].copy()
    st.session_state.cartes_jouees = []
    st.session_state.ordre_cartes_jouees = []
    st.session_state.sorts_prepares = []
    st.session_state.sorts_lances_ce_tour = []
    st.session_state.defausse = []
    st.session_state.aether = 0
    st.session_state.tour = 1
    st.session_state.diamond_cluster_joues = 0
    st.session_state.tours_supplementaires = 0
    st.session_state.quartz_derniere_revelation = "Aucune"
    st.session_state.aether_gemme = 0
    st.session_state.attaques_nemesis_bloquees = 0
    st.session_state.charges = 0
    st.session_state.charges_max = 4 if nom_mage in {"Jian", "Reeve"} else 5
    st.session_state.pulsations = 0
    st.session_state.degats_infliges = 0
    st.session_state.vie = 10
    st.session_state.vie_max = 10
    st.session_state.cartes_detruites = []
    st.session_state.cartes_transmises = []
    st.session_state.serviteurs_silences = 0
    st.session_state.effets_allies_en_attente = []
    st.session_state.reliques_jouees = []
    st.session_state.gravehold = 30
    st.session_state.gravehold_max = 30
    st.session_state.cube_actif = False
    st.session_state.cube_cout_max = None
    st.session_state.ombre_utilisee_par_breche = {}
    st.session_state.lava_tendril_utilise_par_breche = {}
    st.session_state.message_regle = ""
    st.session_state.journal_tours = []
    st.session_state.achats_ce_tour = []
    st.session_state.kadir_double_preparation_tour = None
    st.session_state.forme_qu = None

    # Une copie independante des breches pour chaque nouvelle partie.
    if nom_mage == "Nym":
        st.session_state.breches = [breche.copy() for breche in BRECHES_NYM]
    elif nom_mage == "Mazra":
        st.session_state.breches = [breche.copy() for breche in BRECHES_MAZRA]
    elif nom_mage == "Z'hana":
        st.session_state.breches = [breche.copy() for breche in BRECHES_ZHANA]
    elif nom_mage == "Reeve":
        st.session_state.breches = [breche.copy() for breche in BRECHES_REEVE]
    elif nom_mage == "Qu":
        st.session_state.breches = [breche.copy() for breche in BRECHES_QU]
    elif nom_mage == "Kadir":
        st.session_state.breches = [breche.copy() for breche in BRECHES_KADIR]
    elif nom_mage == "Xaxos":
        st.session_state.breches = [breche.copy() for breche in BRECHES_XAXOS]
    elif nom_mage == "Brama":
        st.session_state.breches = [breche.copy() for breche in BRECHES_BRAMA]
    elif nom_mage == "Adelheim":
        st.session_state.breches = [breche.copy() for breche in BRECHES_ADELHEIM]
    elif nom_mage == "Jian":
        st.session_state.breches = [breche.copy() for breche in BRECHES_JIAN]
    elif nom_mage == "Lash":
        st.session_state.breches = [breche.copy() for breche in BRECHES_LASH]
    elif nom_mage == "Mist":
        st.session_state.breches = [breche.copy() for breche in BRECHES_LASH]
    elif nom_mage == "Phaedraxa":
        st.session_state.breches = [breche.copy() for breche in BRECHES_PHAEDRAXA]
    else:
        st.session_state.breches = []

    for breche in st.session_state.breches:
        breche["focus_ce_tour"] = False


def activer_pouvoir_kadir(indices_defausse):
    if st.session_state.mage_actuel != "Kadir":
        return
    if st.session_state.charges < 5:
        return

    positions = sorted(set(indices_defausse[:3]), reverse=True)
    cartes_reprises = []
    for position in positions:
        if 0 <= position < len(st.session_state.defausse):
            carte = st.session_state.defausse[position]
            if CARTES.get(carte, {}).get("type") in {"sort", "sort_marche"}:
                cartes_reprises.append(st.session_state.defausse.pop(position))

    if not cartes_reprises:
        return

    # Restore the selected display order in hand.
    st.session_state.main.extend(reversed(cartes_reprises))
    st.session_state.charges -= 5
    st.session_state.kadir_double_preparation_tour = st.session_state.tour
    st.session_state.message_regle = (
        f"Pouvoir de Kadir : {len(cartes_reprises)} sort(s) repris en main. "
        "Chaque brèche ouverte peut préparer jusqu'à deux sorts ce tour."
    )


def basculer_forme_qu():
    if st.session_state.mage_actuel != "Qu":
        return
    if st.session_state.forme_qu is None:
        st.session_state.message_regle = "Choisis d'abord la forme initiale de Qu."
        return
    st.session_state.forme_qu = (
        "Builder"
        if st.session_state.forme_qu == "Destroyer"
        else "Destroyer"
    )


def jouer_change_form(index, forme_initiale=None):
    if index < 0 or index >= len(st.session_state.main) or st.session_state.main[index] != "Change Form":
        return
    st.session_state.main.pop(index)
    st.session_state.reliques_jouees.append("Change Form")
    st.session_state.ordre_cartes_jouees.append("Change Form")
    if st.session_state.forme_qu is None:
        if forme_initiale not in {"Builder", "Destroyer"}:
            return
        st.session_state.forme_qu = forme_initiale
    else:
        basculer_forme_qu()
    st.session_state.message_regle = f"Change Form : Qu est en forme {st.session_state.forme_qu}."

def jouer_melded_radite(index):
    if index < 0 or index >= len(st.session_state.main) or st.session_state.main[index] != "Melded Radite":
        return
    st.session_state.main.pop(index)
    gain = 1 if st.session_state.forme_qu == "Builder" else 0
    st.session_state.aether += gain
    st.session_state.cartes_jouees.append("Melded Radite")
    st.session_state.ordre_cartes_jouees.append("Melded Radite")
    st.session_state.message_regle = (
        f"Melded Radite : +{gain} Æther. L'effet permettant de lancer le sort préparé d'un allié reste à résoudre manuellement."
    )


def activer_pouvoir_qu_destroyer(indices_sorts):
    if st.session_state.mage_actuel != "Qu" or st.session_state.forme_qu != "Destroyer" or st.session_state.charges < 5:
        return
    for index in sorted(set(indices_sorts[:2]), reverse=True):
        if 0 <= index < len(st.session_state.sorts_prepares):
            # Le pouvoir autorise un lancement pendant la phase principale.
            st.session_state.sorts_prepares[index]["tour_preparation"] = st.session_state.tour - 1
            lancer_sort(index)
    st.session_state.charges -= 5
    basculer_forme_qu()
    st.session_state.message_regle = "Duality Embrace : sorts lancés, Qu passe en forme Builder."


def activer_pouvoir_qu_builder(selections):
    if st.session_state.mage_actuel != "Qu" or st.session_state.forme_qu != "Builder" or st.session_state.charges < 5:
        return
    places = [i for i,b in enumerate(st.session_state.breches) if b.get("ouverte") and len(indices_sorts_dans_breche(i)) < capacite_breche(i)]
    prepares = 0
    for position in sorted(set(selections[:2]), reverse=True):
        if not places or not (0 <= position < len(st.session_state.defausse)):
            continue
        carte = st.session_state.defausse[position]
        if CARTES.get(carte, {}).get("type") not in {"sort", "sort_marche"}:
            continue
        carte = st.session_state.defausse.pop(position)
        breche = places.pop(0)
        st.session_state.sorts_prepares.append({"carte": carte, "tour_preparation": st.session_state.tour, "breche": breche})
        prepares += 1
    if prepares == 0:
        return
    st.session_state.charges -= 5
    basculer_forme_qu()
    st.session_state.message_regle = f"Duality Embrace : {prepares} sort(s) préparé(s), Qu passe en forme Destroyer."

def activer_pouvoir_brama():
    if st.session_state.mage_actuel != "Brama" or st.session_state.charges < 5 or st.session_state.vie >= st.session_state.vie_max:
        return
    soin = min(4, st.session_state.vie_max - st.session_state.vie)
    st.session_state.charges -= 5
    st.session_state.vie += soin
    st.session_state.message_regle = f"Pouvoir de Brama : {soin} PV récupéré(s)."

def activer_pouvoir_adelheim():
    if st.session_state.mage_actuel != "Adelheim":
        return
    if st.session_state.charges < 5:
        return
    st.session_state.charges -= 5
    st.session_state.attaques_nemesis_bloquees += 1
    st.session_state.message_regle = (
        "Aethereal Ward : l'attaque ou la carte Pouvoir de la Némésis est défaussée sans effet."
    )


def activer_black_mirror(index_sort):
    if st.session_state.mage_actuel != "Jian":
        return
    if st.session_state.charges < 4:
        return
    if index_sort < 0 or index_sort >= len(st.session_state.sorts_prepares):
        return

    sort_prepare = st.session_state.sorts_prepares.pop(index_sort)
    carte = sort_prepare["carte"]
    index_breche = sort_prepare.get("breche")

    degats_base = CARTES.get(carte, {}).get("degats", 0)
    bonus_breche = 0
    if index_breche is not None and 0 <= index_breche < len(st.session_state.breches):
        breche = st.session_state.breches[index_breche]
        if breche.get("ouverte", False):
            bonus_breche = breche.get("bonus_degats", 0)

    degats_par_lancement = degats_base + bonus_breche
    degats_total = degats_par_lancement * 2
    st.session_state.degats_infliges += degats_total
    st.session_state.charges -= 4

    if carte == "Force colossale":
        st.session_state.serviteurs_silences += 2
    elif carte == "Invoque-débris":
        st.session_state.effets_allies_en_attente.extend([
            "Un allié reprend en main une carte de sa défausse coûtant 0 Æther.",
            "Un allié reprend en main une carte de sa défausse coûtant 0 Æther.",
        ])
    elif carte == "Faux de désintégration":
        st.session_state.vie = max(0, st.session_state.vie - 2)
        st.session_state.cartes_transmises.append(carte)
        st.session_state.message_regle = (
            f"Black Mirror avec Faux de désintégration : {degats_total} dégâts, "
            "2 PV perdus, carte transmise à un autre joueur."
        )
        return

    st.session_state.sorts_lances_ce_tour.insert(0, carte)
    st.session_state.message_regle = (
        f"Black Mirror : {carte} lancé deux fois pour {degats_total} dégâts au total."
    )


def piocher_carte_pouvoir_mist():
    # Reforme le deck avec la défausse si nécessaire, sans mélanger.
    if len(st.session_state.deck) == 0:
        if len(st.session_state.defausse) == 0:
            return False
        st.session_state.deck = list(reversed(st.session_state.defausse))
        st.session_state.defausse = []

    st.session_state.main.append(st.session_state.deck.pop(0))
    return True


def activer_pouvoir_mist():
    if st.session_state.mage_actuel != "Mist":
        return
    if st.session_state.charges < 5:
        return

    st.session_state.charges -= 5
    nombre_pioche = 0
    for _ in range(4):
        if piocher_carte_pouvoir_mist():
            nombre_pioche += 1
        else:
            break

    st.session_state.message_regle = (
        f"Pouvoir de Mist : {nombre_pioche} carte(s) supplémentaire(s) piochée(s)."
    )


def focaliser_breche(index):
    breche = st.session_state.breches[index]

    if breche["ouverte"]:
        return

    cout = breche["cout_focus"]
    if st.session_state.aether < cout:
        return

    st.session_state.aether -= cout
    breche["focus_ce_tour"] = True

    derniere_etape = len(breche["couts_ouverture"]) - 1

    # Une focalisation fait d'abord avancer la brèche vers le prochain coût.
    # Elle ne s'ouvre que si elle était DÉJÀ sur sa dernière orientation.
    # Exemple Brèche IV : 7 -> 4 -> OUVERTE.
    if breche["etape"] >= derniere_etape:
        breche["ouverte"] = True
    else:
        breche["etape"] += 1


def ouvrir_breche(index):
    breche = st.session_state.breches[index]

    if breche["ouverte"]:
        return

    cout = breche["couts_ouverture"][breche["etape"]]
    if st.session_state.aether < cout:
        return

    st.session_state.aether -= cout
    breche["ouverte"] = True


def jouer_moonstone_shard(index):
    if index < 0 or index >= len(st.session_state.main):
        return
    if st.session_state.main[index] != "Moonstone Shard":
        return

    carte = st.session_state.main.pop(index)
    st.session_state.aether += 1
    st.session_state.aether_gemme += 1
    st.session_state.cartes_jouees.append(carte)
    st.session_state.ordre_cartes_jouees.append(carte)
    st.session_state.message_regle = (
        "Moonstone Shard : +1 Æther et +1 Æther réservé à l'achat d'une gemme."
    )


def jouer_quartz_shard(index, type_revele, placement):
    if index < 0 or index >= len(st.session_state.main):
        return
    if st.session_state.main[index] != "Quartz Shard":
        return

    carte = st.session_state.main.pop(index)
    gain = 2 if type_revele == "Joueur" else 1
    st.session_state.aether += gain
    st.session_state.cartes_jouees.append(carte)
    st.session_state.ordre_cartes_jouees.append(carte)
    st.session_state.quartz_derniere_revelation = f"{type_revele} placé en {placement}"
    st.session_state.message_regle = (
        f"Quartz Shard : +{gain} Æther(s). Carte d'ordre {type_revele.lower()} "
        f"conservée {placement}."
    )


def activer_quicken_thought():
    if st.session_state.mage_actuel != "Lash":
        return
    if st.session_state.charges < 5:
        return
    if st.session_state.vie <= 0:
        return

    st.session_state.charges -= 5
    st.session_state.vie = max(0, st.session_state.vie - 1)
    st.session_state.tours_supplementaires += 1
    st.session_state.message_regle = (
        "Quicken Thought : carte d'ordre du joueur remélangée, 1 PV perdu. "
        "Un tour supplémentaire est à résoudre."
    )


def appliquer_modificateur_gemme_qu(gain):
    if st.session_state.mage_actuel != "Qu":
        return gain
    if st.session_state.forme_qu == "Builder":
        return gain + 1
    if st.session_state.forme_qu == "Destroyer":
        return max(0, gain - 1)
    return gain


def jouer_diamond_cluster(index):
    if index < 0 or index >= len(st.session_state.main):
        return
    if st.session_state.main[index] != "Diamond Cluster":
        return

    carte = st.session_state.main.pop(index)
    st.session_state.diamond_cluster_joues += 1

    # Premier Diamond Cluster : 2 Æthers de base.
    # Le deuxième joué ce tour gagne +2 Æthers conditionnels.
    # Le modificateur de Qu s'applique une seule fois par gemme jouée.
    # Builder : 3 puis 5, soit 8 Æthers au total.
    gain_base = 2
    bonus_deuxieme = 2 if st.session_state.diamond_cluster_joues == 2 else 0
    gain = appliquer_modificateur_gemme_qu(gain_base + bonus_deuxieme)
    st.session_state.aether += gain
    st.session_state.cartes_jouees.append(carte)
    st.session_state.ordre_cartes_jouees.append(carte)

    if st.session_state.diamond_cluster_joues == 2:
        st.session_state.message_regle = (
            f"Diamond Cluster : deuxième joué ce tour, +{gain} Æthers."
        )
    else:
        st.session_state.message_regle = f"Diamond Cluster : +{gain} Æthers."


def jouer_lurking_sionite(index):
    if index < 0 or index >= len(st.session_state.main):
        return
    if st.session_state.main[index] != "Lurking Sionite":
        return

    bonus = 1 if "Lurking Sionite" in st.session_state.defausse else 0
    gain = appliquer_modificateur_gemme_qu(2 + bonus)

    carte = st.session_state.main.pop(index)
    st.session_state.aether += gain
    st.session_state.cartes_jouees.append(carte)
    st.session_state.ordre_cartes_jouees.append(carte)

    if bonus:
        st.session_state.message_regle = (
            f"Lurking Sionite : +{gain} Æthers, avec le bonus conditionnel."
        )
    else:
        st.session_state.message_regle = f"Lurking Sionite : +{gain} Æthers."


def jouer_tourmaline_shard(index_tourmaline, index_detruire=None):
    if index_tourmaline < 0 or index_tourmaline >= len(st.session_state.main):
        return
    if st.session_state.main[index_tourmaline] != "Tourmaline Shard":
        return

    if index_detruire is not None:
        if index_detruire == index_tourmaline or st.session_state.vie <= 0:
            return
        carte_detruite = st.session_state.main[index_detruire]
        for position in sorted([index_tourmaline, index_detruire], reverse=True):
            st.session_state.main.pop(position)
        st.session_state.vie = max(0, st.session_state.vie - 1)
        st.session_state.cartes_detruites.append(carte_detruite)
    else:
        st.session_state.main.pop(index_tourmaline)

    st.session_state.aether += 1
    st.session_state.cartes_jouees.append("Tourmaline Shard")
    st.session_state.ordre_cartes_jouees.append("Tourmaline Shard")


def jouer_obsidian_shard(index, subir_degats=False):
    if index < 0 or index >= len(st.session_state.main):
        return
    if st.session_state.main[index] != "Obsidian Shard":
        return
    if subir_degats and st.session_state.vie <= 0:
        return

    carte = st.session_state.main.pop(index)
    gain = 3 if subir_degats else 1
    if subir_degats:
        st.session_state.vie = max(0, st.session_state.vie - 1)

    st.session_state.aether += gain
    st.session_state.cartes_jouees.append(carte)
    st.session_state.ordre_cartes_jouees.append(carte)
    st.session_state.message_regle = (
        f"Obsidian Shard : +{gain} Æther(s)"
        + (" et 1 PV perdu." if subir_degats else ".")
    )


def activer_recherche_mazra_retour():
    cartes = [c for c in st.session_state.defausse if c.startswith("Mazra's ")]
    if st.session_state.mage_actuel != "Mazra" or st.session_state.charges < 4 or not cartes:
        return
    st.session_state.charges -= 4
    st.session_state.defausse = [c for c in st.session_state.defausse if not c.startswith("Mazra's ")]
    st.session_state.main.extend(cartes)
    st.session_state.message_regle = f"Research : {len(cartes)} carte(s) de Mazra reprise(s) en main."


def activer_recherche_mazra_amelioration(index_main, nouvelle_carte):
    couts = {"Mazra's Studies": 0, "Mazra's Arc": 3, "Mazra's Wisdom": 3, "Mazra's Gift": 6, "Mazra's Inferno": 6}
    if st.session_state.mage_actuel != "Mazra" or st.session_state.charges < 4:
        return
    if not (0 <= index_main < len(st.session_state.main)):
        return
    ancienne = st.session_state.main[index_main]
    if not ancienne.startswith("Mazra's ") or couts.get(nouvelle_carte) != couts.get(ancienne, -99) + 3:
        return
    st.session_state.charges -= 4
    st.session_state.main.pop(index_main)
    st.session_state.cartes_detruites.append(ancienne)
    st.session_state.main.append(nouvelle_carte)
    st.session_state.message_regle = f"Research : {ancienne} détruite, {nouvelle_carte} ajoutée à la main."


def jouer_gemme(index):
    carte = st.session_state.main.pop(index)
    aether_produit = CARTES[carte]["aether"]
    if st.session_state.mage_actuel == "Qu":
        if st.session_state.forme_qu == "Builder":
            aether_produit += 1
        elif st.session_state.forme_qu == "Destroyer":
            aether_produit = max(0, aether_produit - 1)

    st.session_state.aether += aether_produit
    st.session_state.cartes_jouees.append(carte)
    st.session_state.ordre_cartes_jouees.append(carte)


def jouer_pointe_de_vide(index_pointe, index_defausse=None):
    # Pointe de vide produit toujours 2 Æthers.
    # Si une autre carte est choisie, cette carte est immédiatement défaussée
    # et Kadir gagne 1 charge.
    if index_pointe < 0 or index_pointe >= len(st.session_state.main):
        return

    if index_defausse is None:
        carte = st.session_state.main.pop(index_pointe)
        gain = appliquer_modificateur_gemme_qu(2)
        st.session_state.aether += gain
        st.session_state.cartes_jouees.append(carte)
        st.session_state.ordre_cartes_jouees.append(carte)
        return

    if index_defausse == index_pointe:
        return
    if index_defausse < 0 or index_defausse >= len(st.session_state.main):
        return
    if st.session_state.charges >= st.session_state.charges_max:
        return

    carte_pointe = st.session_state.main[index_pointe]
    carte_defaussee = st.session_state.main[index_defausse]

    # Retirer les deux cartes sans décaler le second index.
    for position in sorted([index_pointe, index_defausse], reverse=True):
        st.session_state.main.pop(position)

    gain = appliquer_modificateur_gemme_qu(2)
    st.session_state.aether += gain
    st.session_state.charges += 1
    st.session_state.cartes_jouees.append(carte_pointe)
    st.session_state.ordre_cartes_jouees.append(carte_pointe)

    # Une carte défaussée par l'effet va immédiatement au-dessus de la défausse.
    st.session_state.defausse.insert(0, carte_defaussee)


def jouer_voltecorce(index, choix):
    # Les deux options produisent toujours 2 Æthers.
    if choix == "depenser_pulsation":
        if st.session_state.pulsations < 1:
            return
        if st.session_state.charges >= st.session_state.charges_max:
            return

    carte = st.session_state.main.pop(index)
    st.session_state.aether += 2

    if choix == "gagner_pulsation":
        st.session_state.pulsations += 1
    else:
        st.session_state.pulsations -= 1
        st.session_state.charges += 1

    st.session_state.cartes_jouees.append(carte)

    st.session_state.ordre_cartes_jouees.append(carte)


def indices_sorts_dans_breche(index_breche):
    return [
        index
        for index, sort_prepare in enumerate(st.session_state.sorts_prepares)
        if sort_prepare.get("breche") == index_breche
    ]


def index_sort_dans_breche(index_breche):
    indices = indices_sorts_dans_breche(index_breche)
    return indices[0] if indices else None


def capacite_breche(index_breche):
    breche = st.session_state.breches[index_breche]
    pouvoir_actif = (
        st.session_state.mage_actuel == "Kadir"
        and st.session_state.kadir_double_preparation_tour == st.session_state.tour
        and breche.get("ouverte", False)
    )
    return 2 if pouvoir_actif else 1


def breches_disponibles_pour_preparer():
    disponibles = []
    for index, breche in enumerate(st.session_state.breches):
        utilisable = breche["ouverte"] or breche.get("focus_ce_tour", False)
        if utilisable and len(indices_sorts_dans_breche(index)) < capacite_breche(index):
            disponibles.append(index)
    return disponibles


def preparer_sort(index_carte, index_breche):
    # Double securite : meme si l'interface se recharge mal,
    # la fonction refuse une breche deja occupee.
    if index_breche not in breches_disponibles_pour_preparer():
        st.session_state.message_regle = "Cette brèche contient déjà un sort."
        return

    carte = st.session_state.main.pop(index_carte)
    st.session_state.sorts_prepares.append({
        "carte": carte,
        "tour_preparation": st.session_state.tour,
        "breche": index_breche,
    })
    st.session_state.message_regle = ""


def activer_lava_tendril_prepare(index_sort):
    """Inflige 1 dégât une fois par tour tant que Lava Tendril est préparé."""
    if index_sort < 0 or index_sort >= len(st.session_state.sorts_prepares):
        return

    sort_prepare = st.session_state.sorts_prepares[index_sort]
    if sort_prepare["carte"] != "Lava Tendril":
        return

    index_breche = sort_prepare.get("breche")
    if index_breche is None:
        return

    if st.session_state.lava_tendril_utilise_par_breche.get(index_breche) == st.session_state.tour:
        return

    st.session_state.degats_infliges += 1
    st.session_state.lava_tendril_utilise_par_breche[index_breche] = st.session_state.tour
    st.session_state.message_regle = (
        "Lava Tendril : 1 dégât infligé à la fin de la phase d'incantation."
    )


def utiliser_ombre_devorante(index_sort, index_carte_main):
    """Détruit une carte de la main, une fois par tour, tant qu'Ombre est préparée."""
    if index_sort < 0 or index_sort >= len(st.session_state.sorts_prepares):
        return

    sort_prepare = st.session_state.sorts_prepares[index_sort]
    if sort_prepare["carte"] != "Ombre Dévorante":
        return

    index_breche = sort_prepare.get("breche")
    if index_breche is None:
        return

    if st.session_state.ombre_utilisee_par_breche.get(index_breche) == st.session_state.tour:
        return

    if index_carte_main < 0 or index_carte_main >= len(st.session_state.main):
        return

    carte_detruite = st.session_state.main.pop(index_carte_main)
    st.session_state.cartes_detruites.append(carte_detruite)
    st.session_state.ombre_utilisee_par_breche[index_breche] = st.session_state.tour
    st.session_state.message_regle = f"Ombre Dévorante : {carte_detruite} a été détruite."


def lancer_cinder(index, choix):
    if index < 0 or index >= len(st.session_state.sorts_prepares):
        return
    sort_prepare = st.session_state.sorts_prepares[index]
    if sort_prepare.get("carte") != "Cinder":
        return
    if st.session_state.tour <= sort_prepare.get("tour_preparation", 0):
        return

    sort_prepare = st.session_state.sorts_prepares.pop(index)
    index_breche = sort_prepare.get("breche")
    bonus_breche = 0
    if index_breche is not None and 0 <= index_breche < len(st.session_state.breches):
        breche = st.session_state.breches[index_breche]
        if breche.get("ouverte", False):
            bonus_breche = breche.get("bonus_degats", 0)

    if choix == "aether":
        st.session_state.aether += 2
        if bonus_breche > 0:
            st.session_state.degats_infliges += bonus_breche
        st.session_state.message_regle = (
            "Cinder : +2 Æthers"
            + (f" et {bonus_breche} dégât de bonus de brèche." if bonus_breche else ".")
        )
    else:
        degats = 1 + bonus_breche
        st.session_state.degats_infliges += degats
        st.session_state.message_regle = f"Cinder : {degats} dégât(s) infligé(s)."
    st.session_state.defausse.insert(0, "Cinder")


def lancer_eternal_ember(index, choix, index_cible=None):
    if index < 0 or index >= len(st.session_state.sorts_prepares):
        return

    ember = st.session_state.sorts_prepares[index]
    if ember.get("carte") != "Eternal Ember":
        return
    if st.session_state.tour <= ember.get("tour_preparation", 0):
        return

    index_breche = ember.get("breche")
    bonus_breche = 0
    if index_breche is not None and 0 <= index_breche < len(st.session_state.breches):
        breche = st.session_state.breches[index_breche]
        if breche.get("ouverte", False):
            bonus_breche = breche.get("bonus_degats", 0)

    if choix == "degats":
        st.session_state.sorts_prepares.pop(index)
        degats = 1 + bonus_breche
        st.session_state.degats_infliges += degats
        st.session_state.defausse.insert(0, "Eternal Ember")
        st.session_state.message_regle = f"Eternal Ember : {degats} dégât(s) infligé(s)."
        return

    if choix != "double" or index_cible is None:
        return
    if index_cible == index or not (0 <= index_cible < len(st.session_state.sorts_prepares)):
        return

    cible = st.session_state.sorts_prepares[index_cible]
    if st.session_state.tour <= cible.get("tour_preparation", 0):
        return

    carte_cible = cible.get("carte")
    degats_cible = CARTES.get(carte_cible, {}).get("degats", 0)
    breche_cible_index = cible.get("breche")
    bonus_cible = 0
    if breche_cible_index is not None and 0 <= breche_cible_index < len(st.session_state.breches):
        breche_cible = st.session_state.breches[breche_cible_index]
        if breche_cible.get("ouverte", False):
            bonus_cible = breche_cible.get("bonus_degats", 0)

    # Le sort ciblé est lancé sans être retiré de sa brèche.
    degats_copie = degats_cible + bonus_cible
    st.session_state.degats_infliges += degats_copie

    # Eternal Ember est ensuite défaussée. Son dégât imprimé est remplacé,
    # mais son éventuel bonus de brèche reste applicable.
    st.session_state.sorts_prepares.pop(index)
    if bonus_breche > 0:
        st.session_state.degats_infliges += bonus_breche
    st.session_state.defausse.insert(0, "Eternal Ember")
    st.session_state.message_regle = (
        f"Eternal Ember : {carte_cible} lancé sans être défaussé "
        f"pour {degats_copie} dégât(s)"
        + (f", plus {bonus_breche} dégât de bonus d'Eternal Ember." if bonus_breche else ".")
    )


def lancer_mazras_studies(index, choix):
    if index < 0 or index >= len(st.session_state.sorts_prepares):
        return

    sort_prepare = st.session_state.sorts_prepares[index]
    if sort_prepare.get("carte") != "Mazra's Studies":
        return
    if st.session_state.tour <= sort_prepare.get("tour_preparation", 0):
        return
    if choix not in {"degats", "focus_iii"}:
        return

    index_breche_sort = sort_prepare.get("breche")
    bonus_breche_sort = 0
    if (
        index_breche_sort is not None
        and 0 <= index_breche_sort < len(st.session_state.breches)
    ):
        breche_sort = st.session_state.breches[index_breche_sort]
        if breche_sort.get("ouverte", False):
            bonus_breche_sort = breche_sort.get("bonus_degats", 0)

    # Mazra gagne une charge si le sort est lancé depuis sa brèche III de Recherche.
    if (
        st.session_state.mage_actuel == "Mazra"
        and index_breche_sort is not None
        and 0 <= index_breche_sort < len(st.session_state.breches)
        and st.session_state.breches[index_breche_sort].get("charge_sur_lancement", False)
    ):
        st.session_state.charges = min(
            st.session_state.charges_max,
            st.session_state.charges + 1
        )

    if choix == "degats":
        degats = 1 + bonus_breche_sort
        st.session_state.degats_infliges += degats
        message = f"Mazra's Studies : {degats} dégât(s) infligé(s)."
    else:
        index_breche_iii = next(
            (
                i
                for i, breche in enumerate(st.session_state.breches)
                if breche.get("numero") == "III"
            ),
            None
        )
        if index_breche_iii is None:
            return

        breche_iii = st.session_state.breches[index_breche_iii]
        if breche_iii.get("ouverte", False):
            return

        derniere_etape = len(breche_iii["couts_ouverture"]) - 1
        if breche_iii["etape"] >= derniere_etape:
            breche_iii["ouverte"] = True
            action_breche = "la brèche III a été ouverte"
        else:
            breche_iii["etape"] += 1
            breche_iii["focus_ce_tour"] = True
            action_breche = "la brèche III a été focalisée gratuitement"

        if bonus_breche_sort > 0:
            st.session_state.degats_infliges += bonus_breche_sort
        message = f"Mazra's Studies : {action_breche}."
        if bonus_breche_sort > 0:
            message += f" Bonus de brèche : {bonus_breche_sort} dégât(s)."

    st.session_state.sorts_prepares.pop(index)
    st.session_state.defausse.insert(0, "Mazra's Studies")
    st.session_state.message_regle = message


def lancer_sort(index):
    sort_prepare = st.session_state.sorts_prepares[index]
    if st.session_state.tour <= sort_prepare["tour_preparation"]:
        return

    sort_prepare = st.session_state.sorts_prepares.pop(index)
    carte = sort_prepare["carte"]
    index_breche = sort_prepare.get("breche")

    degats_base = CARTES.get(carte, {}).get("degats", 0)
    bonus_breche = 0
    if index_breche is not None and 0 <= index_breche < len(st.session_state.breches):
        breche = st.session_state.breches[index_breche]
        if breche.get("ouverte", False):
            bonus_breche = breche.get("bonus_degats", 0)

    if (
        st.session_state.mage_actuel == "Mazra"
        and index_breche is not None
        and 0 <= index_breche < len(st.session_state.breches)
        and st.session_state.breches[index_breche].get("charge_sur_lancement", False)
    ):
        st.session_state.charges = min(
            st.session_state.charges_max,
            st.session_state.charges + 1
        )

    degats_total = degats_base + bonus_breche
    if st.session_state.mage_actuel == "Qu":
        if st.session_state.forme_qu == "Destroyer":
            degats_total += 1
        elif st.session_state.forme_qu == "Builder":
            degats_total = max(0, degats_total - 1)
    if degats_total > 0:
        st.session_state.degats_infliges += degats_total

    if carte == "Force colossale":
        st.session_state.serviteurs_silences += 1
        st.session_state.message_regle = (
            f"Force colossale : {degats_total} dégâts infligés à la Némésis "
            "et 1 serviteur réduit au silence."
        )

    elif carte == "Invoque-débris":
        st.session_state.effets_allies_en_attente.append(
            "Un allié reprend en main une carte de sa défausse coûtant 0 Æther."
        )
        st.session_state.message_regle = (
            f"Invoque-débris : {degats_total} dégâts infligés. "
            "Effet allié à résoudre."
        )

    elif carte == "Ombre Dévorante":
        st.session_state.message_regle = (
            f"Ombre Dévorante : {degats_total} dégâts infligés."
        )

    elif carte == "Faux de désintégration":
        st.session_state.vie = max(0, st.session_state.vie - 1)
        st.session_state.cartes_transmises.append(carte)
        st.session_state.message_regle = (
            f"Faux de désintégration : {degats_total} dégâts infligés, "
            "1 PV perdu, carte transmise à un autre joueur."
        )
        return

    elif degats_total > 0:
        detail_bonus = f" dont +{bonus_breche} de brèche" if bonus_breche else ""
        st.session_state.message_regle = (
            f"{carte} : {degats_total} dégâts infligés{detail_bonus}."
        )

    st.session_state.sorts_lances_ce_tour.insert(0, carte)

def cout_carte(nom):
    for cartes in MARCHE.values():
        for info in cartes:
            if info["nom"] == nom:
                return info["cout"]
    return 0


def terminer_relique(index, detruire=False):
    carte = st.session_state.main.pop(index)
    if detruire:
        st.session_state.cartes_detruites.append(carte)
    else:
        # Même fonctionnement visuel que les gemmes :
        # la relique sort de la main et apparaît immédiatement dans
        # l'aperçu de la défausse, tout en conservant l'ordre de jeu.
        st.session_state.reliques_jouees.append(carte)
        st.session_state.ordre_cartes_jouees.append(carte)

def stabiliser_breche_gratuitement(index_breche):
    breche = st.session_state.breches[index_breche]
    if breche["ouverte"]: return
    derniere = len(breche["couts_ouverture"]) - 1
    if breche["etape"] >= derniere: breche["ouverte"] = True
    else: breche["etape"] += 1
    breche["focus_ce_tour"] = True


def jouer_bottled_vortex(index_relique, selections):
    # selections contient des identifiants ('main', index) ou ('defausse', index).
    selections_uniques = []
    for selection in selections:
        if selection not in selections_uniques:
            selections_uniques.append(selection)
    selections_uniques = selections_uniques[:2]

    if index_relique < 0 or index_relique >= len(st.session_state.main):
        return
    if st.session_state.main[index_relique] != "Bottled Vortex":
        return

    # Bottled Vortex est détruit en premier.
    st.session_state.main.pop(index_relique)
    st.session_state.cartes_detruites.append("Bottled Vortex")

    # Ajuster les indices de main après le retrait de Bottled Vortex.
    main_indices = []
    defausse_indices = []
    for zone, position in selections_uniques:
        if zone == "main":
            if position == index_relique:
                continue
            position_corrigee = position - 1 if position > index_relique else position
            if 0 <= position_corrigee < len(st.session_state.main):
                main_indices.append(position_corrigee)
        elif zone == "defausse":
            if 0 <= position < len(st.session_state.defausse):
                defausse_indices.append(position)

    # Détruire depuis les indices les plus élevés pour éviter les décalages.
    for position in sorted(set(main_indices), reverse=True):
        st.session_state.cartes_detruites.append(st.session_state.main.pop(position))
    for position in sorted(set(defausse_indices), reverse=True):
        st.session_state.cartes_detruites.append(st.session_state.defausse.pop(position))

    # Piocher une carte. Si nécessaire, retourner la défausse sans mélanger.
    if len(st.session_state.deck) == 0 and len(st.session_state.defausse) > 0:
        st.session_state.deck = list(reversed(st.session_state.defausse))
        st.session_state.defausse = []

    if len(st.session_state.deck) > 0:
        st.session_state.main.append(st.session_state.deck.pop(0))

    st.session_state.message_regle = (
        f"Bottled Vortex détruit : {len(selections_uniques)} autre(s) carte(s) "
        "sélectionnée(s), puis 1 carte piochée."
    )


def jouer_relique_simple(index, effet):
    if effet == "etoile": st.session_state.charges = min(5, st.session_state.charges + 3)
    elif effet == "talisman": st.session_state.charges = min(5, st.session_state.charges + 1)
    elif effet == "filaments":
        st.session_state.pulsations += 1
        if st.session_state.pulsations >= 2: st.session_state.charges = min(5, st.session_state.charges + 1)
    elif effet == "cube":
        st.session_state.aether += 1; st.session_state.cube_actif = True
    terminer_relique(index)


def jouer_puits(index, cible):
    if cible == "gravehold": st.session_state.gravehold = min(st.session_state.gravehold_max, st.session_state.gravehold + 2)
    else: st.session_state.vie = min(st.session_state.vie_max, st.session_state.vie + 2)
    terminer_relique(index)


def jouer_transmogrifieur(index_relique, index_detruire, gain):
    if index_relique == index_detruire: return
    cout_detruit = cout_carte(st.session_state.main[index_detruire])
    if cout_carte(gain) > cout_detruit + 3: return
    detruite = st.session_state.main[index_detruire]
    for pos in sorted([index_relique,index_detruire], reverse=True): st.session_state.main.pop(pos)
    st.session_state.cartes_detruites.append(detruite)
    st.session_state.reliques_jouees.append("Transmogrifieur")
    st.session_state.ordre_cartes_jouees.append("Transmogrifieur")
    # La carte gagnée est acquise après la résolution de la relique,
    # elle arrive donc au-dessus de Transmogrifieur.
    st.session_state.defausse.insert(0, gain)


def acheter_charge():
    if st.session_state.aether >= 2 and st.session_state.charges < 5:
        st.session_state.aether -= 2
        st.session_state.charges += 1


def obtenir_charge():
    if st.session_state.charges < 5:
        st.session_state.charges += 1


def retirer_charge():
    if st.session_state.charges > 0:
        st.session_state.charges -= 1

def est_une_gemme_du_marche(nom_carte):
    return any(info["nom"] == nom_carte for info in MARCHE.get("Gemmes", []))


def peut_acheter_carte(nom_carte, cout):
    if est_une_gemme_du_marche(nom_carte):
        return st.session_state.aether + st.session_state.aether_gemme >= cout
    return st.session_state.aether >= cout


def acheter_carte(nom_carte, cout):
    # Pour une gemme, l'Æther réservé de Moonstone Shard peut compléter le paiement.
    if not peut_acheter_carte(nom_carte, cout):
        return

    if est_une_gemme_du_marche(nom_carte):
        paiement_normal = min(st.session_state.aether, cout)
        st.session_state.aether -= paiement_normal
        reste = cout - paiement_normal
        st.session_state.aether_gemme -= reste
    else:
        st.session_state.aether -= cout

    st.session_state.achats_ce_tour.append(f"{nom_carte} ({cout} Æthers)")

    if st.session_state.cube_actif:
        st.session_state.cube_cout_max = max(0, cout - 1)
        st.session_state.cube_actif = False

    if nom_carte == "Ambre de V'risbois":
        # Regle demandee : a l'achat, Ambre va automatiquement
        # sur le dessus du deck. La position 0 est le dessus du deck.
        st.session_state.deck.insert(0, nom_carte)
    else:
        # Les autres cartes achetees vont normalement au-dessus
        # de la defausse.
        st.session_state.defausse.insert(0, nom_carte)


def creer_resume_tour():
    sorts_prepares_ce_tour = []
    for sort_prepare in st.session_state.sorts_prepares:
        if sort_prepare.get("tour_preparation") == st.session_state.tour:
            index_breche = sort_prepare.get("breche")
            numero_breche = "?"
            if index_breche is not None and 0 <= index_breche < len(st.session_state.breches):
                numero_breche = st.session_state.breches[index_breche]["numero"]
            sorts_prepares_ce_tour.append(
                f"{sort_prepare['carte']} (brèche {numero_breche})"
            )

    return {
        "tour": st.session_state.tour,
        "mage": st.session_state.mage_actuel,
        "cartes_jouees": st.session_state.cartes_jouees.copy(),
        "reliques_jouees": st.session_state.reliques_jouees.copy(),
        "sorts_prepares": sorts_prepares_ce_tour,
        "sorts_lances": st.session_state.sorts_lances_ce_tour.copy(),
        "achats": st.session_state.achats_ce_tour.copy(),
        "main_fin": st.session_state.main.copy(),
    }


def journal_html():
    def ligne(titre, valeurs):
        contenu = " → ".join(valeurs) if valeurs else "Aucun"
        return f"<div><strong>{titre} :</strong> {contenu}</div>"

    blocs = []
    for entree in st.session_state.journal_tours:
        blocs.append(
            "<section class='tour'>"
            f"<h2>Tour {entree['tour']} · {entree['mage']}</h2>"
            + ligne("Cartes jouées", entree["cartes_jouees"])
            + ligne("Reliques jouées", entree["reliques_jouees"])
            + ligne("Sorts préparés", entree["sorts_prepares"])
            + ligne("Sorts lancés", entree["sorts_lances"])
            + ligne("Achats", entree["achats"])
            + ligne("Cartes en main", entree["main_fin"])
            + "</section>"
        )

    contenu = "".join(blocs) or "<p>Aucun tour enregistré.</p>"
    return f"""<!doctype html>
<html lang='fr'><head><meta charset='utf-8'><title>Journal Aeon's End</title>
<style>body{{font-family:Arial,sans-serif;margin:24px;color:#111}}h1{{font-size:22px}}.tour{{border:1px solid #bbb;border-radius:8px;padding:12px;margin-bottom:12px}}.tour h2{{font-size:16px;margin:0 0 8px}}.tour div{{margin:4px 0;font-size:13px}}@media print{{button{{display:none}}body{{margin:8mm}}}}</style>
</head><body><h1>Journal de partie Aeon's End</h1>{contenu}<script>window.onload=()=>window.print();</script></body></html>"""


def imprimer_journal():
    components.html(journal_html(), height=1, scrolling=False)


def terminer_tour():
    st.session_state.journal_tours.append(creer_resume_tour())

    # À la fin du tour, les gemmes jouées sont placées au-dessus.
    # Les sorts lancés ce tour se retrouvent juste en dessous.
    # Exemple : Emerald Shard + 3 Crystal, puis Spark lancé
    # donne [Emerald Shard, Crystal, Crystal, Crystal, Spark].
    # La liste interne a le DESSUS de la défausse en premier : la dernière
    # gemme jouée finit donc tout en haut, la première jouée en dessous.
    st.session_state.defausse = (
        list(reversed(st.session_state.ordre_cartes_jouees))
        + st.session_state.sorts_lances_ce_tour
        + st.session_state.defausse
    )

    # Les zones temporaires du tour sont vidées
    st.session_state.cartes_jouees = []
    st.session_state.reliques_jouees = []
    st.session_state.ordre_cartes_jouees = []
    st.session_state.sorts_lances_ce_tour = []

    # Piocher jusqu'à avoir 5 cartes en main
    while len(st.session_state.main) < 5:

        # Si le deck est vide, on retourne la défausse
        if len(st.session_state.deck) == 0:

            # Si la défausse est également vide, la pioche s'arrête
            if len(st.session_state.defausse) == 0:
                break

            # La défausse est retournée pour former le nouveau deck
            st.session_state.deck = list(
                reversed(st.session_state.defausse)
            )

            # La défausse est maintenant vide
            st.session_state.defausse = []

        # La première carte du deck est piochée
        carte_piochee = st.session_state.deck.pop(0)

        # La carte piochée rejoint la main
        st.session_state.main.append(carte_piochee)

    for breche in st.session_state.breches:
        breche["focus_ce_tour"] = False

    # Les Æthers restants sont perdus.
    st.session_state.aether = 0
    st.session_state.aether_gemme = 0

    st.session_state.diamond_cluster_joues = 0
    st.session_state.achats_ce_tour = []

    # Passage au tour suivant
    st.session_state.tour += 1


# --------------------------------------------------
# INTERFACE
# --------------------------------------------------

mage_choisi = st.selectbox(
    "Choisir un mage",
    list(MAGES.keys())
)

# Première ouverture de l'application
if "mage_actuel" not in st.session_state:
    initialiser_partie(mage_choisi)

# Changement de mage
if mage_choisi != st.session_state.mage_actuel:
    initialiser_partie(mage_choisi)
    st.rerun()

if "charges" not in st.session_state:
    st.session_state.charges = 0
if "charges_max" not in st.session_state:
    st.session_state.charges_max = 5
if "pulsations" not in st.session_state:
    st.session_state.pulsations = 0
if "degats_infliges" not in st.session_state:
    st.session_state.degats_infliges = 0
if "vie" not in st.session_state:
    st.session_state.vie = 10
if "vie_max" not in st.session_state:
    st.session_state.vie_max = 10
if "cartes_transmises" not in st.session_state:
    st.session_state.cartes_transmises = []
if "serviteurs_silences" not in st.session_state:
    st.session_state.serviteurs_silences = 0
if "effets_allies_en_attente" not in st.session_state:
    st.session_state.effets_allies_en_attente = []
if "cartes_detruites" not in st.session_state:
    st.session_state.cartes_detruites = []
if "ombre_utilisee_par_breche" not in st.session_state:
    st.session_state.ombre_utilisee_par_breche = {}
if "lava_tendril_utilise_par_breche" not in st.session_state:
    st.session_state.lava_tendril_utilise_par_breche = {}
if "message_regle" not in st.session_state:
    st.session_state.message_regle = ""
for breche in st.session_state.breches:
    breche.setdefault("focus_ce_tour", False)
for sort_prepare in st.session_state.sorts_prepares:
    sort_prepare.setdefault("breche", None)

# Compatibilité avec une session déjà ouverte avant l'ajout des charges.
if "charges" not in st.session_state:
    st.session_state.charges = 0
if "charges_max" not in st.session_state:
    st.session_state.charges_max = 5
if "pulsations" not in st.session_state:
    st.session_state.pulsations = 0
if "degats_infliges" not in st.session_state:
    st.session_state.degats_infliges = 0
if "vie" not in st.session_state:
    st.session_state.vie = 10
if "vie_max" not in st.session_state:
    st.session_state.vie_max = 10
if "cartes_transmises" not in st.session_state:
    st.session_state.cartes_transmises = []
if "cartes_detruites" not in st.session_state:
    st.session_state.cartes_detruites = []
if "ombre_utilisee_par_breche" not in st.session_state:
    st.session_state.ombre_utilisee_par_breche = {}
for breche in st.session_state.breches:
    if "focus_ce_tour" not in breche:
        breche["focus_ce_tour"] = False

if "reliques_jouees" not in st.session_state:
    st.session_state.reliques_jouees = []
if "gravehold" not in st.session_state:
    st.session_state.gravehold, st.session_state.gravehold_max = 30, 30
if "cube_actif" not in st.session_state:
    st.session_state.cube_actif, st.session_state.cube_cout_max = False, None

if "attaques_nemesis_bloquees" not in st.session_state:
    st.session_state.attaques_nemesis_bloquees = 0

if "aether_gemme" not in st.session_state:
    st.session_state.aether_gemme = 0
if st.session_state.mage_actuel in {"Jian", "Reeve", "Mazra"}:
    st.session_state.charges_max = 4

if "tours_supplementaires" not in st.session_state:
    st.session_state.tours_supplementaires = 0
if "quartz_derniere_revelation" not in st.session_state:
    st.session_state.quartz_derniere_revelation = "Aucune"

if "diamond_cluster_joues" not in st.session_state:
    st.session_state.diamond_cluster_joues = 0

if "journal_tours" not in st.session_state:
    st.session_state.journal_tours = []
if "achats_ce_tour" not in st.session_state:
    st.session_state.achats_ce_tour = []

if "ordre_cartes_jouees" not in st.session_state:
    st.session_state.ordre_cartes_jouees = []

if "kadir_double_preparation_tour" not in st.session_state:
    st.session_state.kadir_double_preparation_tour = None
if "forme_qu" not in st.session_state:
    st.session_state.forme_qu = None

# Action principale toujours visible en haut de la partie
col_fin_tour, col_impression = st.columns([20, 1])
with col_fin_tour:
    if st.button(
        "⏭️ Terminer le tour", type="primary",
        use_container_width=True, key="terminer_tour_haut"
    ):
        terminer_tour()
        st.rerun()
with col_impression:
    if st.button("🖨️", key="imprimer_journal_tours", help="Imprimer le journal", use_container_width=True):
        imprimer_journal()

# En-tête de la partie
col_tour, col_aether, col_pulsations, col_charges, col_reset = st.columns([1, 1, 1, 2, 2])

with col_tour:
    st.metric("Tour", st.session_state.tour)

with col_aether:
    st.metric("Æthers disponibles", st.session_state.aether)

with col_pulsations:
    if mage_choisi == "Kadir":
        st.metric("💠 Pulsations", st.session_state.pulsations)

with col_charges:
    if mage_choisi in {"Kadir", "Adelheim", "Jian", "Lash", "Mist", "Brama", "Xaxos", "Qu", "Phaedraxa", "Reeve", "Z'hana", "Mazra", "Nym"}:
        st.markdown(f"**⚡ Charges : {st.session_state.charges}/{st.session_state.charges_max}**")
        st.progress(st.session_state.charges / st.session_state.charges_max)
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("Acheter", key="acheter_charge", disabled=(st.session_state.aether < 2 or st.session_state.charges >= st.session_state.charges_max), use_container_width=True):
                acheter_charge()
                st.rerun()
        with c2:
            if st.button("Obtenir +1", key="obtenir_charge", disabled=st.session_state.charges >= st.session_state.charges_max, use_container_width=True):
                obtenir_charge()
                st.rerun()
        with c3:
            if st.button("Retirer −1", key="retirer_charge", disabled=st.session_state.charges == 0, use_container_width=True):
                retirer_charge()
                st.rerun()

with col_reset:
    if st.button("🔄 Réinitialiser la partie", use_container_width=True):
        initialiser_partie(mage_choisi)
        st.rerun()

forme_qu_texte = (
    f" · 🌓 Forme : **{st.session_state.forme_qu}**"
    if mage_choisi == "Qu" and st.session_state.forme_qu is not None
    else (" · 🌓 Forme : **à choisir**" if mage_choisi == "Qu" else "")
)
st.caption(
    f"Mage actif : **{mage_choisi}**{forme_qu_texte} · "
    f"❤️ PV : **{st.session_state.vie}/{st.session_state.vie_max}** · "
    f"💥 Dégâts infligés : **{st.session_state.degats_infliges}** · "
    f"💠 Pulsations : **{st.session_state.pulsations}** · "
    f"🌙 Æther gemme : **{st.session_state.aether_gemme}** · "
    f"🏰 Gravehold : **{st.session_state.gravehold}/{st.session_state.gravehold_max}** · "
    f"🤫 Silences : **{st.session_state.serviteurs_silences}**"
)

if mage_choisi == "Kadir":
    options_sorts_kadir = {
        f"{position + 1}. {carte}": position
        for position, carte in enumerate(st.session_state.defausse)
        if CARTES.get(carte, {}).get("type") in {"sort", "sort_marche"}
    }

    choix_sorts_kadir = st.multiselect(
        "Sorts dans la défausse",
        list(options_sorts_kadir.keys()),
        max_selections=3,
        key="choix_pouvoir_kadir",
        placeholder="Sélectionner jusqu'à trois sorts"
    )

    if st.button(
        "✨ Activer le pouvoir",
        key="pouvoir_kadir",
        disabled=(
            st.session_state.charges < 5
            or len(choix_sorts_kadir) == 0
        ),
        use_container_width=True
    ):
        activer_pouvoir_kadir([
            options_sorts_kadir[choix]
            for choix in choix_sorts_kadir
        ])
        st.rerun()

if mage_choisi == "Brama":
    if st.button("❤️ Activer le pouvoir · récupérer jusqu’à 4 PV", key="pouvoir_brama", disabled=(st.session_state.charges < 5 or st.session_state.vie >= st.session_state.vie_max), use_container_width=True):
        activer_pouvoir_brama(); st.rerun()
if mage_choisi == "Xaxos":
    if st.button("✨ Activer le pouvoir · effet alliés", key="pouvoir_xaxos_allies", disabled=st.session_state.charges < 5, use_container_width=True):
        st.session_state.charges -= 5
        st.session_state.message_regle = "Pouvoir de Xaxos activé : effet à appliquer avec les alliés."
        st.rerun()
if mage_choisi == "Qu":
    if st.button(
        "🌓 Activer le pouvoir",
        key="pouvoir_qu_manuel",
        disabled=st.session_state.charges < 5,
        use_container_width=True
    ):
        st.session_state.charges -= 5
        st.session_state.message_regle = (
            "Pouvoir de Qu activé : effet à résoudre manuellement."
        )
        st.rerun()

if mage_choisi == "Adelheim":
    col_pouvoir_adelheim, col_blocages_adelheim = st.columns([4, 1])
    with col_pouvoir_adelheim:
        if st.button(
            "🛡️ Activer le pouvoir",
            key="pouvoir_adelheim",
            disabled=st.session_state.charges < 5,
            use_container_width=True
        ):
            activer_pouvoir_adelheim()
            st.rerun()
    with col_blocages_adelheim:
        st.caption(f"Cartes bloquées : **{st.session_state.attaques_nemesis_bloquees}**")

if mage_choisi == "Jian":
    if st.button(
        "🪞 Activer le pouvoir",
        key="activer_pouvoir_jian_allies",
        disabled=st.session_state.charges < 4,
        use_container_width=True
    ):
        st.session_state.charges -= 4
        st.session_state.message_regle = "Pouvoir de Jian activé : effet à appliquer avec les alliés."
        st.rerun()

if mage_choisi == "Lash":
    col_pouvoir_lash, col_tours_lash = st.columns([4, 1])
    with col_pouvoir_lash:
        if st.button(
            "⚡ Activer le pouvoir",
            key="pouvoir_lash",
            disabled=st.session_state.charges < 5 or st.session_state.vie <= 0,
            use_container_width=True
        ):
            activer_quicken_thought()
            st.rerun()
    with col_tours_lash:
        st.caption(f"Tours bonus : **{st.session_state.tours_supplementaires}**")

if mage_choisi == "Mist":
    if st.button(
        "✨ Activer le pouvoir",
        key="pouvoir_mist",
        disabled=st.session_state.charges < 5,
        use_container_width=True
    ):
        activer_pouvoir_mist()
        st.rerun()

if mage_choisi == "Nym":
    if st.button(
        "🔥 Activer Terminus Barrier",
        key="pouvoir_nym",
        disabled=st.session_state.charges < 5,
        use_container_width=True
    ):
        st.session_state.charges -= 5
        st.session_state.message_regle = (
            "Terminus Barrier : défaussez la première carte du deck Némésis. "
            "Si c'est une Attaque, défaussez une carte supplémentaire."
        )
        st.rerun()

if mage_choisi == "Reeve":
    if st.button(
        "🗡️ Activer Quelling Blade",
        key="pouvoir_reeve",
        disabled=st.session_state.charges < 4,
        use_container_width=True
    ):
        st.session_state.charges -= 4
        st.session_state.message_regle = (
            "Quelling Blade : infligez 5 dégâts à un serviteur, puis "
            "3 dégâts à un autre serviteur. Résolution manuelle."
        )
        st.rerun()

if mage_choisi == "Mazra":
    mazra_en_main = {
        f"{i + 1}. {carte}": i
        for i, carte in enumerate(st.session_state.main)
        if carte.startswith("Mazra's ")
    }
    options_upgrade = {
        "Mazra's Studies": ["Mazra's Arc", "Mazra's Wisdom"],
        "Mazra's Arc": ["Mazra's Gift", "Mazra's Inferno"],
        "Mazra's Wisdom": ["Mazra's Gift", "Mazra's Inferno"],
    }
    if mazra_en_main:
        choix_source = st.selectbox("Carte de Mazra à améliorer", list(mazra_en_main), key="mazra_source")
        index_source = mazra_en_main[choix_source]
        source = st.session_state.main[index_source]
        ameliorations = options_upgrade.get(source, [])
        if ameliorations:
            choix_upgrade = st.selectbox("Amélioration", ameliorations, key="mazra_upgrade")
            if st.button("📚 Research · améliorer", key="pouvoir_mazra_upgrade", disabled=st.session_state.charges < 4, use_container_width=True):
                activer_recherche_mazra_amelioration(index_source, choix_upgrade)
                st.rerun()
    cartes_mazra_defausse = [c for c in st.session_state.defausse if c.startswith("Mazra's ")]
    if st.button(
        "📚 Research · reprendre toutes les cartes Mazra de la défausse",
        key="pouvoir_mazra_retour",
        disabled=(st.session_state.charges < 4 or not cartes_mazra_defausse),
        use_container_width=True
    ):
        activer_recherche_mazra_retour()
        st.rerun()

if mage_choisi == "Z'hana":
    if st.button(
        "🏰 Activer Sanctum Glyph · +7 PV Gravehold",
        key="pouvoir_zhana",
        disabled=st.session_state.charges < 5,
        use_container_width=True
    ):
        soin_gravehold = min(
            7,
            st.session_state.gravehold_max - st.session_state.gravehold
        )
        st.session_state.charges -= 5
        st.session_state.gravehold += soin_gravehold
        if soin_gravehold > 0:
            st.session_state.message_regle = (
                f"Sanctum Glyph : Gravehold récupère {soin_gravehold} PV."
            )
        else:
            st.session_state.message_regle = (
                "Sanctum Glyph activé : Gravehold est déjà à son maximum de PV."
            )
        st.rerun()

if mage_choisi == "Phaedraxa":
    if st.button(
        "🛡️ Activer le pouvoir",
        key="pouvoir_phaedraxa",
        disabled=st.session_state.charges < 5,
        use_container_width=True
    ):
        st.session_state.charges -= 5
        st.session_state.message_regle = (
            "Pouvoir de Phaedraxa activé : prévenir tous les dégâts aux joueurs "
            "et à Gravehold pendant ce tour."
        )
        st.rerun()

if st.session_state.message_regle:
    st.error(st.session_state.message_regle)

st.divider()

# --------------------------------------------------
# BRECHES
# --------------------------------------------------

if mage_choisi in {"Kadir", "Adelheim", "Jian", "Lash", "Brama", "Xaxos", "Mist", "Phaedraxa", "Qu", "Reeve", "Z'hana", "Mazra", "Nym"}:
    st.subheader("🌀 Brèches")
    colonnes_breches = st.columns(len(st.session_state.breches))

    for index, breche in enumerate(st.session_state.breches):
        with colonnes_breches[index]:
            numero = breche["numero"]
            sorts_indices = indices_sorts_dans_breche(index)
            sort_index = sorts_indices[0] if sorts_indices else None
            sorts_dans_breche = [
                st.session_state.sorts_prepares[i]["carte"]
                for i in sorts_indices
            ]
            sort_dans_breche = sorts_dans_breche[0] if sorts_dans_breche else None

            if breche["ouverte"]:
                bonus = breche["bonus_degats"]
                texte_bonus = f" · +{bonus} dégât" if bonus > 0 else ""
                st.success(f"**Brèche {numero}** · OUVERTE{texte_bonus}")
                if sorts_dans_breche:
                    for sort_nom in sorts_dans_breche:
                        st.warning(f"🔥 {sort_nom}")
                    places_restantes = capacite_breche(index) - len(sorts_dans_breche)
                    if places_restantes > 0:
                        st.caption(f"{places_restantes} emplacement restant")
                else:
                    st.caption(f"Libre · {capacite_breche(index)} sort(s) maximum")
            else:
                etape = breche["etape"]
                cout_ouverture = breche["couts_ouverture"][etape]
                cout_focus = breche["cout_focus"]

                st.warning(
                    f"**Brèche {numero}** · FERMÉE\n\n"
                    f"Ouverture : {cout_ouverture} Æthers"
                )

                col_focus, col_ouvrir = st.columns(2)

                with col_focus:
                    if st.button(
                        f"Focus · {cout_focus}",
                        key=f"focus_breche_{index}",
                        disabled=st.session_state.aether < cout_focus,
                        use_container_width=True
                    ):
                        focaliser_breche(index)
                        st.rerun()

                with col_ouvrir:
                    if st.button(
                        f"Ouvrir · {cout_ouverture}",
                        key=f"ouvrir_breche_{index}",
                        disabled=st.session_state.aether < cout_ouverture,
                        use_container_width=True
                    ):
                        ouvrir_breche(index)
                        st.rerun()

            # Actions des sorts directement sur la brèche
            for position_sort, index_sort_reel in enumerate(sorts_indices):
                sort_prepare = st.session_state.sorts_prepares[index_sort_reel]
                carte_preparee = sort_prepare["carte"]
                tour_preparation = sort_prepare["tour_preparation"]

                if len(sorts_indices) > 1:
                    st.caption(f"Sort {position_sort + 1} : {carte_preparee}")

                if carte_preparee == "Cinder" and st.session_state.tour > tour_preparation:
                    bonus_cinder = breche.get("bonus_degats", 0) if breche.get("ouverte", False) else 0
                    col_cinder_degats, col_cinder_aether = st.columns(2)
                    with col_cinder_degats:
                        if st.button(
                            f"🔥 Lancer · {1 + bonus_cinder} dégât(s)",
                            key=f"cinder_degats_{index}_{index_sort_reel}",
                            use_container_width=True
                        ):
                            lancer_cinder(index_sort_reel, "degats")
                            st.rerun()
                    with col_cinder_aether:
                        texte_cinder_aether = "+2 Æthers"
                        if bonus_cinder:
                            texte_cinder_aether += f" · +{bonus_cinder} dégât"
                        if st.button(
                            f"💎 Lancer · {texte_cinder_aether}",
                            key=f"cinder_aether_{index}_{index_sort_reel}",
                            use_container_width=True
                        ):
                            lancer_cinder(index_sort_reel, "aether")
                            st.rerun()

                if carte_preparee == "Mazra's Studies" and st.session_state.tour > tour_preparation:
                    bonus_studies = (
                        breche.get("bonus_degats", 0)
                        if breche.get("ouverte", False)
                        else 0
                    )
                    index_breche_iii = next(
                        (
                            i
                            for i, breche_info in enumerate(st.session_state.breches)
                            if breche_info.get("numero") == "III"
                        ),
                        None
                    )
                    breche_iii_disponible = (
                        index_breche_iii is not None
                        and not st.session_state.breches[index_breche_iii].get("ouverte", False)
                    )

                    col_studies_degats, col_studies_focus = st.columns(2)
                    with col_studies_degats:
                        if st.button(
                            f"🔥 Lancer · {1 + bonus_studies} dégât(s)",
                            key=f"studies_degats_{index}_{index_sort_reel}",
                            use_container_width=True
                        ):
                            lancer_mazras_studies(index_sort_reel, "degats")
                            st.rerun()

                    with col_studies_focus:
                        texte_focus = "🎯 Focaliser gratuitement la brèche III"
                        if index_breche_iii is not None:
                            breche_iii = st.session_state.breches[index_breche_iii]
                            derniere_etape = len(breche_iii["couts_ouverture"]) - 1
                            if breche_iii.get("etape", 0) >= derniere_etape:
                                texte_focus = "🔓 Ouvrir gratuitement la brèche III"
                        if st.button(
                            texte_focus,
                            key=f"studies_focus_{index}_{index_sort_reel}",
                            disabled=not breche_iii_disponible,
                            use_container_width=True
                        ):
                            lancer_mazras_studies(index_sort_reel, "focus_iii")
                            st.rerun()

                if carte_preparee == "Eternal Ember" and st.session_state.tour > tour_preparation:
                    bonus_ember = breche.get("bonus_degats", 0) if breche.get("ouverte", False) else 0
                    options_ember = {
                        f"{i + 1}. {sort_info['carte']}": i
                        for i, sort_info in enumerate(st.session_state.sorts_prepares)
                        if i != index_sort_reel
                        and st.session_state.tour > sort_info.get("tour_preparation", 0)
                    }

                    if st.button(
                        f"🔥 Lancer · {1 + bonus_ember} dégât(s)",
                        key=f"eternal_ember_degats_{index}_{index_sort_reel}",
                        use_container_width=True
                    ):
                        lancer_eternal_ember(index_sort_reel, "degats")
                        st.rerun()

                    if options_ember:
                        choix_ember = st.selectbox(
                            "Sort à lancer sans le défausser",
                            list(options_ember.keys()),
                            key=f"eternal_ember_cible_{index}_{index_sort_reel}"
                        )
                        texte_bonus_ember = (
                            f" · +{bonus_ember} dégât Eternal Ember"
                            if bonus_ember else ""
                        )
                        if st.button(
                            f"♻️ Lancer le sort sélectionné sans le défausser{texte_bonus_ember}",
                            key=f"eternal_ember_double_{index}_{index_sort_reel}",
                            use_container_width=True
                        ):
                            lancer_eternal_ember(
                                index_sort_reel,
                                "double",
                                options_ember[choix_ember]
                            )
                            st.rerun()
                    else:
                        st.caption("Aucun autre sort préparé disponible.")

                if carte_preparee == "Lava Tendril":
                    lava_deja_utilise = (
                        st.session_state.lava_tendril_utilise_par_breche.get(index)
                        == st.session_state.tour
                    )
                    if not lava_deja_utilise and st.button(
                        "🌋 Fin d'incantation · +1 dégât",
                        key=f"lava_prepare_{index}_{index_sort_reel}",
                        use_container_width=True
                    ):
                        activer_lava_tendril_prepare(index_sort_reel)
                        st.rerun()

                if carte_preparee == "Ombre Dévorante":
                    deja_utilisee = (
                        st.session_state.ombre_utilisee_par_breche.get(index)
                        == st.session_state.tour
                    )
                    if deja_utilisee:
                        st.success("Affinage déjà utilisé ce tour")
                    elif len(st.session_state.main) > 0:
                        options_destruction = {
                            f"{position + 1}. {nom}": position
                            for position, nom in enumerate(st.session_state.main)
                        }
                        choix_destruction = st.selectbox(
                            "Carte à détruire",
                            list(options_destruction.keys()),
                            key=f"ombre_choix_{index}_{index_sort_reel}"
                        )
                        if st.button(
                            "🗑️ Détruire une carte",
                            key=f"ombre_detruire_{index}_{index_sort_reel}",
                            use_container_width=True
                        ):
                            utiliser_ombre_devorante(
                                index_sort_reel,
                                options_destruction[choix_destruction]
                            )
                            st.rerun()

                if st.session_state.tour == tour_preparation:
                    st.caption("Préparé ce tour · lancement au prochain tour")
                elif carte_preparee not in {"Eternal Ember", "Mazra's Studies", "Cinder"} and st.button(
                    f"🔥 Lancer {carte_preparee}",
                    key=f"lancer_depuis_breche_{index}_{index_sort_reel}_{carte_preparee}",
                    use_container_width=True
                ):
                    lancer_sort(index_sort_reel)
                    st.rerun()

    st.divider()

# --------------------------------------------------
# MAIN ET DECK
# --------------------------------------------------

colonne_main = st.container()

with colonne_main:
    st.subheader("🖐️ Main")

    if len(st.session_state.main) == 0:
        st.info("La main est vide.")

    else:
        # Copie nécessaire, car les boutons peuvent modifier la liste
        main_affichee = st.session_state.main.copy()

        # Grille de cinq cartes par ligne. Mist peut monter jusqu'à neuf cartes
        # en main après l'activation de son pouvoir.
        nombre_colonnes_main = 5
        lignes_cartes = [
            main_affichee[position:position + nombre_colonnes_main]
            for position in range(0, len(main_affichee), nombre_colonnes_main)
        ]

        for numero_ligne, cartes_ligne in enumerate(lignes_cartes):
            colonnes_cartes = st.columns(nombre_colonnes_main)

            for position_ligne, carte in enumerate(cartes_ligne):
                # Conserver l'index réel dans la main pour les actions des cartes.
                index = numero_ligne * nombre_colonnes_main + position_ligne
                type_carte = CARTES[carte]["type"]

                with colonnes_cartes[position_ligne]:

                    # Affichage automatique de l'image de la carte
                    chemin_image = image_carte(carte)
                    if chemin_image is not None:
                        st.image(
                            chemin_image,
                            width=145
                        )

                    # Nom et informations de la carte
                    if type_carte == "tourmaline_shard":
                        st.info("💎 **Tourmaline Shard**\n\n+1 Æther")
                        if st.button(
                            "Jouer · +1 Æther",
                            key=f"tourmaline_simple_{index}",
                            use_container_width=True
                        ):
                            jouer_tourmaline_shard(index)
                            st.rerun()

                    elif type_carte == "lurking_sionite":
                        bonus_sionite = 1 if "Lurking Sionite" in st.session_state.defausse else 0
                        gain_sionite = appliquer_modificateur_gemme_qu(2 + bonus_sionite)
                        st.info(
                            f"💎 **Lurking Sionite**\n\n"
                            f"+{gain_sionite} Æthers"
                        )
                        if st.button(
                            f"Jouer · +{gain_sionite} Æthers",
                            key=f"jouer_lurking_sionite_{index}",
                            use_container_width=True
                        ):
                            jouer_lurking_sionite(index)
                            st.rerun()

                    elif type_carte == "diamond_cluster":
                        gain_base_diamond = 2
                        bonus_diamond = 2 if st.session_state.diamond_cluster_joues == 1 else 0
                        prochain_gain = appliquer_modificateur_gemme_qu(
                            gain_base_diamond + bonus_diamond
                        )
                        st.info(
                            f"💎 **Diamond Cluster**\n\n"
                            f"+{prochain_gain} Æthers"
                        )
                        if st.button(
                            f"Jouer · +{prochain_gain} Æthers",
                            key=f"jouer_diamond_cluster_{index}",
                            use_container_width=True
                        ):
                            jouer_diamond_cluster(index)
                            st.rerun()

                    elif type_carte == "quartz_shard":
                        st.info("🔮 **Quartz Shard**\n\nRévélez la carte d'ordre du tour")
                        type_revele = st.radio(
                            "Type révélé",
                            ["Joueur", "Némésis"],
                            key=f"quartz_type_{index}",
                            horizontal=True
                        )
                        placement = st.radio(
                            "Placement",
                            ["au-dessus", "en dessous"],
                            key=f"quartz_place_{index}",
                            horizontal=True
                        )
                        gain_quartz = 2 if type_revele == "Joueur" else 1
                        if st.button(
                            f"Jouer · +{gain_quartz} Æther(s)",
                            key=f"jouer_quartz_{index}",
                            use_container_width=True
                        ):
                            jouer_quartz_shard(index, type_revele, placement)
                            st.rerun()

                    elif type_carte == "moonstone_shard":
                        st.info("🌙 **Moonstone Shard**\n\n+1 Æther · +1 pour une gemme")
                        if st.button(
                            "Jouer",
                            key=f"jouer_moonstone_{index}",
                            use_container_width=True
                        ):
                            jouer_moonstone_shard(index)
                            st.rerun()

                    elif type_carte == "change_form":
                        if st.session_state.forme_qu is None:
                            st.info("🌓 **Change Form**\n\nChoisis la forme initiale")
                            col_builder, col_destroyer = st.columns(2)
                            with col_builder:
                                if st.button("🏗️ Jouer · Builder", key=f"change_form_builder_{index}", use_container_width=True):
                                    jouer_change_form(index, "Builder")
                                    st.rerun()
                            with col_destroyer:
                                if st.button("⚔️ Jouer · Destroyer", key=f"change_form_destroyer_{index}", use_container_width=True):
                                    jouer_change_form(index, "Destroyer")
                                    st.rerun()
                        else:
                            forme_suivante = "Builder" if st.session_state.forme_qu == "Destroyer" else "Destroyer"
                            st.info(f"🌓 **Change Form**\n\n{st.session_state.forme_qu} → {forme_suivante}")
                            if st.button(f"Jouer · passer en {forme_suivante}", key=f"change_form_{index}", use_container_width=True):
                                jouer_change_form(index)
                                st.rerun()

                    elif type_carte == "melded_radite":
                        gain_radite = 1 if st.session_state.forme_qu == "Builder" else 0
                        st.info(f"💎 **Melded Radite**\n\n+{gain_radite} Æther · sort allié manuel")
                        if st.button(f"Jouer · +{gain_radite} Æther", key=f"melded_radite_{index}", use_container_width=True):
                            jouer_melded_radite(index); st.rerun()
                    elif type_carte == "obsidian_shard":
                        st.info(
                            "💎 **Obsidian Shard**\n\n"
                            "+1 Æther, ou perdre 1 PV pour gagner +3 Æthers"
                        )
                        if st.button(
                            "Jouer · +1 Æther",
                            key=f"obsidian_simple_{index}",
                            use_container_width=True
                        ):
                            jouer_obsidian_shard(index, False)
                            st.rerun()
                        if st.button(
                            "Jouer · -1 PV · +3 Æthers",
                            key=f"obsidian_bonus_{index}",
                            disabled=st.session_state.vie <= 0,
                            use_container_width=True
                        ):
                            jouer_obsidian_shard(index, True)
                            st.rerun()

                    elif type_carte == "gemme":
                        aether = CARTES[carte]["aether"]
                        if st.session_state.mage_actuel == "Qu":
                            if st.session_state.forme_qu == "Builder":
                                aether += 1
                            elif st.session_state.forme_qu == "Destroyer":
                                aether = max(0, aether - 1)

                        st.info(
                            f"💎 **{carte}**\n\n"
                            f"+{aether} Æther"
                        )

                        if st.button(
                            "Jouer",
                            key=f"jouer_{index}_{carte}",
                            use_container_width=True
                        ):
                            jouer_gemme(index)
                            st.rerun()

                    elif type_carte in {"sort", "eternal_ember", "cinder"}:
                        st.warning(
                            f"🔥 **{carte}**\n\n"
                            f"Sort"
                        )

                        breches_libres = breches_disponibles_pour_preparer()
                        if not breches_libres:
                            st.button("Aucune brèche libre", key=f"aucune_{index}_{carte}", disabled=True, use_container_width=True)
                        else:
                            choix = {f"Brèche {st.session_state.breches[b]['numero']}": b for b in breches_libres}
                            nom_breche = st.selectbox("Choisir une brèche", list(choix.keys()), key=f"breche_{index}_{carte}", label_visibility="collapsed")
                            if st.button("Préparer", key=f"preparer_{index}_{carte}", use_container_width=True):
                                preparer_sort(index, choix[nom_breche])
                                st.rerun()

                    elif type_carte == "pointe_de_vide":
                        gain_pointe = appliquer_modificateur_gemme_qu(2)
                        st.info(
                            f"💎 **{carte}**\n\n"
                            f"+{gain_pointe} Æthers"
                        )

                        if st.button(
                            f"Jouer · +{gain_pointe} Æthers",
                            key=f"pointe_simple_{index}",
                            use_container_width=True
                        ):
                            jouer_pointe_de_vide(index)
                            st.rerun()

                        autres_cartes = [
                            (position, nom)
                            for position, nom in enumerate(st.session_state.main)
                            if position != index
                        ]

                        if autres_cartes:
                            options_defausse = {
                                f"{position + 1}. {nom}": position
                                for position, nom in autres_cartes
                            }
                            choix_defausse = st.selectbox(
                                "Carte à défausser pour gagner 1 charge",
                                list(options_defausse.keys()),
                                key=f"pointe_defausse_{index}"
                            )

                            if st.button(
                                f"Jouer · +{gain_pointe} Æthers · défausser · +1 Charge",
                                key=f"pointe_charge_{index}",
                                disabled=st.session_state.charges >= st.session_state.charges_max,
                                use_container_width=True
                            ):
                                jouer_pointe_de_vide(
                                    index,
                                    options_defausse[choix_defausse]
                                )
                                st.rerun()
                        else:
                            st.caption("Aucune autre carte en main à défausser.")

                    elif type_carte == "voltecorce":
                        gain_voltecorce = appliquer_modificateur_gemme_qu(2)
                        st.info(
                            f"💎 **{carte}**\n\n"
                            f"Choisissez un effet · +{gain_voltecorce} Æthers"
                        )

                        if st.button(
                            f"+{gain_voltecorce} Æthers · +1 Pulsation",
                            key=f"voltecorce_pulsation_{index}",
                            use_container_width=True
                        ):
                            jouer_voltecorce(index, "gagner_pulsation")
                            st.rerun()

                        if st.button(
                            f"+{gain_voltecorce} Æthers · −1 Pulsation · +1 Charge",
                            key=f"voltecorce_charge_{index}",
                            disabled=(
                                st.session_state.pulsations < 1
                                or st.session_state.charges >= st.session_state.charges_max
                            ),
                            use_container_width=True
                        ):
                            jouer_voltecorce(index, "depenser_pulsation")
                            st.rerun()

                    elif type_carte == "bottled_vortex":
                        st.info("🌀 **Bottled Vortex**\n\nDétruisez jusqu'à 2 cartes, puis piochez 1 carte")

                        options_vortex = {}
                        for position, nom in enumerate(st.session_state.main):
                            if position != index:
                                options_vortex[f"Main · {position + 1}. {nom}"] = ("main", position)
                        for position, nom in enumerate(st.session_state.defausse):
                            options_vortex[f"Défausse · {position + 1}. {nom}"] = ("defausse", position)

                        choix_vortex = st.multiselect(
                            "Cartes à détruire (0 à 2)",
                            list(options_vortex.keys()),
                            max_selections=2,
                            key=f"vortex_choix_{index}"
                        )

                        if st.button(
                            "Détruire Bottled Vortex et résoudre",
                            key=f"vortex_jouer_{index}",
                            use_container_width=True
                        ):
                            jouer_bottled_vortex(
                                index,
                                [options_vortex[choix] for choix in choix_vortex]
                            )
                            st.rerun()

                    elif type_carte == "orbe_stabilisation":
                        fermees = [i for i,b in enumerate(st.session_state.breches) if not b["ouverte"]]
                        choix = {f"Brèche {st.session_state.breches[i]['numero']}":i for i in fermees}
                        if choix:
                            b = st.selectbox("Brèche à stabiliser", list(choix), key=f"orb_{index}")
                            if st.button("Stabiliser", key=f"orb_s_{index}", use_container_width=True):
                                stabiliser_breche_gratuitement(choix[b]); terminer_relique(index); st.rerun()
                        if st.button("Détruire · Gravehold +3", key=f"orb_d_{index}", use_container_width=True):
                            st.session_state.gravehold=min(30,st.session_state.gravehold+3); terminer_relique(index,True); st.rerun()
                    elif type_carte == "etoile_miniature":
                        if st.button("Gagner 3 charges", key=f"etoile_{index}", use_container_width=True): jouer_relique_simple(index,"etoile"); st.rerun()
                    elif type_carte == "talisman_mage":
                        if st.button("Gagner 1 charge", key=f"talisman_{index}", use_container_width=True): jouer_relique_simple(index,"talisman"); st.rerun()
                        st.caption("Charge de l'allié non simulée")
                    elif type_carte == "filaments_ame":
                        if st.button("+1 Pulsation", key=f"fil_{index}", use_container_width=True): jouer_relique_simple(index,"filaments"); st.rerun()
                    elif type_carte == "puits_energie":
                        if st.button("Gravehold +2", key=f"puits_g_{index}", use_container_width=True): jouer_puits(index,"gravehold"); st.rerun()
                        if st.button("Joueur +2 PV", key=f"puits_j_{index}", use_container_width=True): jouer_puits(index,"joueur"); st.rerun()
                    elif type_carte == "cube_sans_fond":
                        if st.button("+1 Æther · activer Cube", key=f"cube_{index}", use_container_width=True): jouer_relique_simple(index,"cube"); st.rerun()
                    elif type_carte == "transmogrifieur":
                        autres=[(i,n) for i,n in enumerate(st.session_state.main) if i!=index]
                        if autres:
                            d={f"{i+1}. {n}":i for i,n in autres}; c=st.selectbox("Carte à détruire",list(d),key=f"trans_d_{index}")
                            limite=cout_carte(st.session_state.main[d[c]])+3
                            gains=[x["nom"] for cats in MARCHE.values() for x in cats if x["cout"]<=limite]
                            if gains:
                                g=st.selectbox(f"Gain gratuit (≤ {limite})",gains,key=f"trans_g_{index}")
                                if st.button("Détruire et gagner",key=f"trans_b_{index}",use_container_width=True): jouer_transmogrifieur(index,d[c],g); st.rerun()
                    elif type_carte in {"gemme_marche", "relique_marche", "sort_marche"}:
                        icone = {
                            "gemme_marche": "💎",
                            "relique_marche": "🧠",
                            "sort_marche": "🔥",
                        }[type_carte]

                        st.info(f"{icone} **{carte}**")
                        st.button(
                            "Effet à intégrer",
                            key=f"effet_non_integre_{index}_{carte}",
                            disabled=True,
                            use_container_width=True
                        )
# --------------------------------------------------
# MARCHÉ
# --------------------------------------------------

st.divider()
st.subheader("🏪 Marché")
st.caption(
    "Les achats sont actifs. Les comportements détaillés des cartes seront "
    "ajoutés progressivement."
)

onglet_gemmes, onglet_reliques, onglet_sorts = st.tabs(
    ["💎 Gemmes", "🧠 Reliques", "🔥 Sorts"]
)

for onglet, categorie in [
    (onglet_gemmes, "Gemmes"),
    (onglet_reliques, "Reliques"),
    (onglet_sorts, "Sorts"),
]:
    with onglet:
        cartes_marche = MARCHE[categorie]
        colonnes_marche = st.columns(len(cartes_marche))

        for index, carte_marche in enumerate(cartes_marche):
            nom = carte_marche["nom"]
            cout = carte_marche["cout"]
            extension = carte_marche["extension"]
            role = carte_marche["role"]

            with colonnes_marche[index]:
                chemin_image = image_carte(nom)
                if chemin_image is not None:
                    st.image(chemin_image, width=165)
                else:
                    st.caption("Image non disponible")

                if st.button(
                    f"Acheter · {cout}",
                    key=f"acheter_{categorie}_{index}_{nom}",
                    disabled=not peut_acheter_carte(nom, cout),
                    use_container_width=True
                ):
                    acheter_carte(nom, cout)
                    st.rerun()

                if st.session_state.cube_cout_max is not None and cout <= st.session_state.cube_cout_max:
                    if st.button("Gratuit via Cube", key=f"cube_gratuit_{categorie}_{index}_{nom}", use_container_width=True):
                        st.session_state.defausse.insert(0, nom)
                        st.session_state.achats_ce_tour.append(f"{nom} (gratuit via Cube)")
                        st.session_state.cube_cout_max = None
                        st.rerun()

# --------------------------------------------------
# ZONES DE JEU
# --------------------------------------------------

st.divider()

colonne_jouees, colonne_defausse = st.columns(2)


with colonne_jouees:
    st.subheader("💎 Gemmes jouées")

    if len(st.session_state.cartes_jouees) == 0:
        st.caption("Aucune gemme jouée.")
    else:
        for position, carte in enumerate(
            st.session_state.cartes_jouees,
            start=1
        ):
            st.write(f"{position}. {carte}")


if len(st.session_state.sorts_lances_ce_tour) > 0:
    with colonne_jouees:
        st.markdown("**🔥 Sorts lancés ce tour :**")
        for carte_lancee in st.session_state.sorts_lances_ce_tour:
            st.write(f"• {carte_lancee}")


if len(st.session_state.cartes_detruites) > 0:
    with colonne_jouees:
        st.markdown("**🗑️ Cartes détruites :**")
        st.caption(" · ".join(st.session_state.cartes_detruites))

if len(st.session_state.cartes_transmises) > 0:
    with colonne_jouees:
        st.markdown("**➡️ Cartes transmises à un autre joueur :**")
        st.caption(" · ".join(st.session_state.cartes_transmises))


if len(st.session_state.effets_allies_en_attente) > 0:
    with colonne_jouees:
        st.markdown("**🤝 Effets alliés à résoudre :**")
        for position, effet in enumerate(st.session_state.effets_allies_en_attente):
            col_effet, col_resolu = st.columns([4, 1])
            with col_effet:
                st.caption(effet)
            with col_resolu:
                if st.button(
                    "Résolu",
                    key=f"effet_allie_resolu_{position}",
                    use_container_width=True
                ):
                    st.session_state.effets_allies_en_attente.pop(position)
                    st.rerun()


with colonne_defausse:
    st.subheader("🗑️ Défausse")

    st.caption(
        "Ordre d'arrivée dans la défausse : la 1re carte est tout en bas "
        "(piochée en premier au retournement), la dernière est au-dessus."
    )

    # Avant la fin du tour, on affiche déjà l'ordre final prévu :
    # gemmes jouées, puis sorts lancés, puis ancienne défausse.
    defausse_affichee = (
        list(reversed(st.session_state.ordre_cartes_jouees))
        + st.session_state.sorts_lances_ce_tour
        + st.session_state.defausse
    )

    if len(defausse_affichee) == 0:
        st.caption("La défausse est vide.")
    else:
        # La liste interne a le dessus de la défausse en premier.
        # On l'affiche dans l'ordre d'arrivée (du fond vers le dessus),
        # ce qui correspond à l'ordre de pioche après retournement.
        ordre_arrivee = list(reversed(defausse_affichee))

        for position, carte in enumerate(ordre_arrivee, start=1):
            if position == len(ordre_arrivee):
                st.write(f"{position}. {carte}  ⬅️ dessus")
            else:
                st.write(f"{position}. {carte}")

# Journal discret des tours
if len(st.session_state.journal_tours) > 0:
    with st.expander(f"🖨️ Journal · {len(st.session_state.journal_tours)} tour(s)", expanded=False):
        for entree in st.session_state.journal_tours:
            cartes = " → ".join(entree["cartes_jouees"]) or "Aucune"
            prepares = " · ".join(entree["sorts_prepares"]) or "Aucun"
            achats = " · ".join(entree["achats"]) or "Aucun"
            main = " · ".join(entree["main_fin"]) or "Vide"
            st.caption(
                f"Tour {entree['tour']} : {cartes} / sorts préparés : {prepares} / "
                f"achats : {achats} / main : {main}"
            )
        if st.button("Vider le journal", key="vider_journal_tours", use_container_width=True):
            st.session_state.journal_tours = []
            st.rerun()


# --------------------------------------------------
# DECK COMPACT — TOUT EN BAS
# --------------------------------------------------

st.divider()

with st.expander(
    f"📚 Deck · {len(st.session_state.deck)} carte(s)",
    expanded=False
):
    st.caption(
        "Lecture de gauche à droite puis ligne suivante. "
        "La carte n° 1 est au-dessus du deck."
    )

    if len(st.session_state.deck) == 0:
        st.caption("Le deck est vide.")
    else:
        nombre_colonnes_deck = 4
        colonnes_deck_compact = st.columns(nombre_colonnes_deck)

        for position, carte in enumerate(st.session_state.deck, start=1):
            colonne = colonnes_deck_compact[(position - 1) % nombre_colonnes_deck]
            with colonne:
                etiquette = "⬆️ " if position == 1 else ""
                st.markdown(
                    f"<div class='deck-card-compact'>"
                    f"<span class='deck-position'>{position}.</span> "
                    f"{etiquette}{carte}</div>",
                    unsafe_allow_html=True
                )

