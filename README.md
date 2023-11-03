# color_palette_generator 

By: Brayam Pineda.

Version: 0.1.0

In this project let's to construct a Color Palette Generator based on prompts using the API of OpenAI

## Create environment

```bash
conda env create -f environment.yml
activate color_palette_generator
```

or 

```bash
mamba env create -f environment.yml
activate color_palette_generator
```

## Project organization

    color_palette_generator
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-initial-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---
