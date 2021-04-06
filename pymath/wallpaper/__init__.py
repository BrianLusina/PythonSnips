def wallpaper(l, w, h):
    wall_area = 2 * ((l * h) + (w * h))
    wall_paper_area = .52 * (10 * 1.15)
    papers = wall_area / wall_paper_area
    return papers
