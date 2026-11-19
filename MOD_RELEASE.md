# Omsk Expansion map mod

The playable mod is generated locally at:

```text
dist/omsk-expansion/
```

Size: about 6.2 GB, 4069 compiled cells.

Maps:

```text
Isilkul, Omsk Oblast                        168 cells
Солнцевка и Водяное, Омская область         252
Омск, Омская область                        930
Краснодар, Краснодарский край               837
Новосибирск, Новосибирская область          1014
Москва                                      868
```

The generated cells are deliberately **not committed to Git**. GitHub rejects
individual files over 100 MB and the repository would be several gigabytes.
Use one of:

1. Git LFS (`git lfs track 'dist/omsk-expansion/**'`) with enough LFS quota;
2. a GitHub Release asset split into <2 GB archives;
3. external storage.

Build source, plans, overlap trimmer and the expansion runner are committed in
this repository.
