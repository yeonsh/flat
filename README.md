flat
====

Rename files under subdirectories to flat names

Original file names:

    ./img/icon/ic_a.png
    ./img/icon/ic_b.png
    ./img/map/map_a.png
    ./img/map/map_b.png
    ./img/map/asia/korea.png
    ./img/map/asia/japan.png

Run *flat*:

    python flat.py img

New file names:

    ./img__icon__ic_a.png
    ./img__icon__ic_b.png
    ./img__map__map_a.png
    ./img__map__map_b.png
    ./img__map__asia__korea.png
    ./img__map__asia__japan.png
