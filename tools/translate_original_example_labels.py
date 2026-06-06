from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BLACK = (30, 30, 30)
RED = (190, 55, 65)
ORANGE = (215, 145, 60)
BLUE = (70, 125, 185)
WHITE = (255, 255, 255)


def font(size):
    for path in (
        "/System/Library/Fonts/Supplemental/ChalkboardSE.ttc",
        "/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf",
        "/System/Library/Fonts/Supplemental/Marker Felt.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


F24 = font(24)
F28 = font(28)
F32 = font(32)
F38 = font(38)


def clear(draw, box):
    draw.rounded_rectangle(box, radius=10, fill=WHITE)


def text(draw, xy, value, color=BLACK, size=28):
    draw.text(xy, value, fill=color, font={24: F24, 28: F28, 32: F32, 38: F38}[size])


def cover(box):
    return {"box": box, "xy": (box[0], box[1]), "text": "", "color": BLACK, "size": 24}


def apply_ops(path, ops):
    im = Image.open(path).convert("RGB")
    draw = ImageDraw.Draw(im)
    for op in ops:
        clear(draw, op["box"])
        text(draw, op["xy"], op["text"], op.get("color", BLACK), op.get("size", 28))
    im.save(path)


def op(box, xy, value, color=BLACK, size=28):
    return {"box": box, "xy": xy, "text": value, "color": color, "size": size}


OPS = {
    "01-two-breakpoints.png": [
        cover((160, 320, 360, 430)),
        cover((500, 245, 655, 335)),
        cover((800, 470, 910, 550)),
        cover((1215, 510, 1345, 625)),
        cover((700, 85, 980, 190)),
        cover((400, 635, 590, 745)),
        cover((1050, 635, 1235, 745)),
        op((130, 125, 250, 185), (145, 135), "input", BLUE, 24),
        op((705, 90, 965, 185), (720, 100), "two breaks", RED, 32),
        op((1035, 175, 1185, 230), (1048, 184), "handoff", BLUE, 24),
        op((180, 330, 330, 420), (194, 346), "before", BLUE, 28),
        op((1030, 330, 1180, 420), (1044, 346), "after", BLUE, 28),
        op((510, 250, 645, 330), (530, 272), "material", BLACK, 28),
        op((810, 480, 900, 545), (824, 496), "content", BLACK, 24),
        op((1240, 520, 1325, 610), (1254, 546), "task", BLACK, 24),
        op((510, 475, 635, 535), (522, 486), "judgment", RED, 24),
        op((875, 420, 955, 470), (884, 429), "gap", BLACK, 24),
        op((420, 650, 570, 735), (432, 666), "material stuck", RED, 28),
        op((1070, 650, 1215, 735), (1082, 666), "no handoff", RED, 28),
        op((1210, 585, 1325, 655), (1222, 598), "drop", RED, 24),
    ],
    "02-sort-by-purpose.png": [
        cover((700, 110, 1035, 255)),
        cover((340, 360, 555, 460)),
        cover((340, 475, 560, 595)),
        cover((340, 610, 565, 730)),
        cover((1170, 270, 1415, 415)),
        cover((1170, 430, 1415, 565)),
        cover((1170, 575, 1420, 725)),
        cover((825, 620, 1135, 740)),
        op((705, 115, 1025, 250), (718, 126), "sort by purpose", RED, 32),
        op((430, 250, 570, 305), (444, 260), "raw notes", BLACK, 24),
        op((345, 365, 540, 455), (372, 392), "external", BLACK, 28),
        op((345, 485, 545, 585), (372, 522), "internal", BLACK, 28),
        op((345, 615, 545, 715), (372, 652), "feedback", BLACK, 28),
        op((1185, 285, 1395, 395), (1200, 304), "traffic", BLACK, 32),
        op((1185, 440, 1395, 545), (1208, 462), "trust", BLACK, 32),
        op((1185, 590, 1405, 700), (1195, 612), "convert", BLACK, 32),
        op((840, 640, 1120, 725), (855, 650), "judge first", BLUE, 32),
    ],
    "03-one-fish-many-uses.png": [
        cover((210, 460, 430, 580)),
        cover((830, 385, 985, 480)),
        cover((1060, 345, 1220, 445)),
        cover((1285, 380, 1445, 480)),
        cover((1460, 480, 1620, 590)),
        cover((870, 615, 1310, 715)),
        cover((890, 685, 1520, 810)),
        op((410, 330, 540, 390), (425, 342), "source", BLACK, 24),
        op((225, 485, 410, 560), (242, 502), "good material", BLACK, 32),
        op((845, 405, 965, 470), (858, 418), "traffic", BLACK, 24),
        op((1080, 365, 1205, 430), (1092, 378), "trust", BLACK, 24),
        op((1305, 400, 1425, 465), (1318, 412), "essay", BLACK, 24),
        op((1480, 505, 1605, 570), (1492, 518), "sales", BLACK, 24),
        op((875, 630, 960, 700), (888, 645), "main", BLACK, 24),
        op((1025, 630, 1125, 700), (1038, 645), "split", BLACK, 24),
        op((1185, 630, 1285, 700), (1198, 645), "reuse", BLACK, 24),
        op((905, 690, 1500, 800), (1050, 720), "one source, many outputs", RED, 28),
    ],
    "04-handoff-path.png": [
        cover((160, 250, 340, 370)),
        cover((635, 260, 825, 375)),
        cover((970, 255, 1130, 365)),
        cover((1285, 240, 1480, 360)),
        cover((1320, 570, 1530, 715)),
        cover((340, 590, 560, 725)),
        op((170, 135, 250, 185), (182, 145), "idea", BLACK, 24),
        op((170, 260, 325, 360), (184, 282), "hook", BLACK, 32),
        op((350, 250, 450, 305), (360, 260), "draft", BLACK, 24),
        op((645, 275, 805, 360), (658, 292), "bridge hook", BLACK, 28),
        op((985, 265, 1115, 350), (998, 282), "knowledge", BLACK, 28),
        op((1300, 250, 1460, 345), (1312, 268), "core lesson", BLACK, 28),
        op((1365, 585, 1510, 700), (1378, 626), "not the end", RED, 28),
        op((360, 600, 540, 710), (378, 626), "new material", BLACK, 28),
    ],
    "05-information-well.png": [
        cover((120, 145, 340, 280)),
        cover((585, 465, 745, 605)),
        cover((115, 620, 320, 745)),
        cover((1140, 380, 1345, 520)),
        cover((1120, 685, 1435, 875)),
        op((135, 160, 330, 265), (148, 182), "info well", BLACK, 32),
        op((600, 480, 730, 590), (612, 512), "first pick", BLACK, 24),
        op((125, 630, 300, 735), (148, 668), "noise", RED, 28),
        op((1160, 395, 1325, 500), (1188, 420), "usable", ORANGE, 28),
        op((1130, 700, 1405, 875), (1160, 755), "today's focus", BLUE, 28),
    ],
    "06-idea-press.png": [
        cover((120, 250, 420, 370)),
        cover((370, 380, 540, 520)),
        cover((690, 130, 890, 240)),
        cover((1100, 420, 1280, 555)),
        cover((1360, 405, 1580, 560)),
        cover((765, 625, 940, 715)),
        op((135, 260, 400, 360), (148, 286), "messy ideas", RED, 32),
        op((385, 405, 520, 500), (402, 430), "ideas", BLACK, 32),
        op((700, 145, 875, 225), (718, 170), "pressure", BLACK, 28),
        op((1120, 445, 1260, 535), (1138, 468), "small test", BLACK, 32),
        op((1370, 430, 1560, 535), (1385, 456), "try it", BLUE, 32),
        op((780, 640, 920, 700), (792, 650), "pressed", BLACK, 24),
    ],
    "07-content-fermentation.png": [
        cover((120, 230, 445, 335)),
        cover((440, 500, 665, 600)),
        cover((980, 415, 1290, 560)),
        cover((1375, 465, 1555, 605)),
        cover((1220, 620, 1450, 830)),
        op((135, 240, 430, 325), (148, 266), "raw notes", RED, 28),
        op((455, 515, 650, 590), (470, 535), "ferment", BLACK, 28),
        op((995, 430, 1270, 545), (1015, 465), "slow ferment", BLACK, 32),
        op((1395, 485, 1535, 585), (1412, 512), "reusable", BLUE, 32),
        op((1240, 635, 1375, 700), (1252, 648), "ready", BLUE, 24),
        op((1280, 740, 1425, 815), (1295, 760), "asset", BLACK, 32),
    ],
    "08-trust-bridge.png": [
        cover((210, 135, 350, 215)),
        cover((365, 225, 555, 365)),
        cover((190, 385, 330, 470)),
        cover((635, 495, 795, 605)),
        cover((785, 545, 950, 635)),
        cover((700, 300, 1050, 470)),
        cover((735, 705, 925, 825)),
        cover((1300, 385, 1465, 465)),
        cover((400, 610, 545, 690)),
        cover((1260, 630, 1455, 720)),
        op((235, 145, 335, 205), (248, 156), "claim", RED, 24),
        op((375, 235, 535, 350), (395, 260), "not just\nshouting", RED, 28),
        op((205, 395, 310, 455), (218, 408), "stranger", BLACK, 24),
        op((645, 505, 780, 590), (658, 520), "customer\nresult +30%", BLACK, 24),
        op((790, 560, 930, 625), (802, 572), "actually useful", BLACK, 24),
        op((720, 315, 1035, 455), (735, 348), "small proof", BLUE, 32),
        op((750, 720, 905, 805), (765, 742), "slow bridge", BLACK, 28),
        op((1320, 395, 1445, 455), (1332, 408), "willing", BLACK, 24),
        op((410, 620, 530, 680), (422, 632), "handoff", BLACK, 24),
        op((1270, 645, 1435, 705), (1282, 656), "trust", RED, 24),
    ],
    "02-minimum-loop.png": [
        cover((150, 185, 335, 300)),
        cover((625, 175, 800, 265)),
        cover((780, 405, 925, 515)),
        cover((925, 175, 1130, 285)),
        cover((1020, 235, 1150, 320)),
        cover((1430, 320, 1585, 420)),
        cover((700, 695, 900, 785)),
        cover((1270, 375, 1390, 455)),
        op((170, 200, 320, 290), (188, 228), "sources", RED, 32),
        op((640, 190, 780, 255), (652, 202), "debug", RED, 24),
        op((800, 420, 900, 500), (815, 440), "judge", RED, 24),
        op((945, 195, 1115, 275), (965, 220), "content", RED, 32),
        op((1030, 250, 1135, 310), (1042, 262), "better", RED, 24),
        op((1445, 330, 1565, 405), (1460, 350), "handoff", RED, 32),
        op((715, 710, 875, 770), (728, 722), "tight loop", BLUE, 24),
        op((1285, 390, 1370, 445), (1296, 400), "ship", RED, 24),
    ],
    "06-three-sources.png": [
        cover((150, 175, 405, 315)),
        cover((150, 365, 405, 465)),
        cover((150, 525, 420, 690)),
        cover((585, 350, 1030, 485)),
        cover((545, 570, 790, 665)),
        cover((600, 750, 805, 860)),
        cover((890, 740, 1180, 885)),
        cover((1310, 720, 1505, 815)),
        op((160, 185, 390, 300), (188, 235), "daily notes", RED, 28),
        op((175, 375, 380, 455), (188, 400), "old docs", ORANGE, 28),
        op((160, 540, 405, 680), (188, 572), "field signals", RED, 28),
        op((600, 360, 820, 470), (610, 382), "method\nnotes", BLACK, 24),
        op((705, 360, 920, 470), (724, 382), "course\ncards", BLACK, 24),
        op((840, 360, 1015, 470), (858, 382), "case\nlibrary", BLACK, 24),
        op((560, 585, 655, 650), (572, 598), "comments", BLACK, 24),
        op((680, 585, 770, 650), (692, 598), "DMs", BLACK, 24),
        op((610, 765, 780, 850), (632, 792), "topic bin", BLACK, 32),
        op((900, 750, 1160, 875), (930, 790), "all in", BLUE, 32),
        op((1325, 735, 1485, 795), (1338, 747), "usable result", BLUE, 24),
    ],
    "07-three-content-jobs.png": [
        cover((485, 335, 660, 450)),
        cover((740, 150, 930, 265)),
        cover((750, 390, 940, 515)),
        cover((750, 640, 950, 765)),
        cover((1240, 105, 1470, 220)),
        cover((1375, 375, 1600, 500)),
        cover((1320, 680, 1560, 810)),
        cover((655, 295, 810, 380)),
        cover((1120, 455, 1290, 550)),
        cover((1235, 700, 1405, 795)),
        op((505, 355, 640, 435), (520, 375), "do not mix", RED, 28),
        op((760, 165, 905, 250), (780, 188), "traffic", ORANGE, 38),
        op((770, 410, 915, 495), (790, 434), "trust", ORANGE, 38),
        op((770, 660, 920, 745), (790, 684), "convert", ORANGE, 38),
        op((1260, 120, 1445, 205), (1280, 144), "seen", BLUE, 38),
        op((1400, 390, 1570, 485), (1415, 420), "trusted", BLUE, 38),
        op((1340, 700, 1535, 790), (1355, 730), "finds you", BLUE, 38),
        op((675, 310, 790, 365), (688, 322), "attention", BLUE, 24),
        op((1140, 475, 1270, 535), (1152, 487), "bridge", BLUE, 24),
        op((1255, 720, 1385, 780), (1267, 732), "action", BLUE, 24),
    ],
    "08-handoff-copy-toolbox.png": [
        cover((640, 195, 1020, 360)),
        cover((80, 490, 320, 575)),
        cover((1175, 490, 1415, 575)),
        cover((205, 610, 325, 700)),
        cover((1310, 610, 1435, 700)),
        cover((555, 390, 695, 470)),
        cover((720, 390, 860, 470)),
        cover((880, 390, 1045, 470)),
        cover((610, 535, 795, 650)),
        cover((795, 535, 980, 650)),
        cover((970, 535, 1160, 650)),
        cover((1110, 160, 1315, 360)),
        op((650, 205, 1000, 350), (664, 235), "handoff toolbox", RED, 32),
        op((95, 505, 300, 565), (112, 520), "finished piece", BLACK, 24),
        op((1190, 505, 1395, 565), (1208, 520), "finished piece", BLACK, 24),
        op((220, 625, 310, 685), (235, 638), "next", RED, 24),
        op((1325, 625, 1420, 685), (1340, 638), "next", RED, 24),
        op((570, 405, 675, 460), (582, 416), "claim", BLACK, 24),
        op((735, 405, 840, 460), (750, 416), "proof", BLACK, 24),
        op((895, 405, 1025, 460), (908, 416), "next", BLACK, 24),
        op((625, 550, 780, 640), (646, 575), "hook", BLACK, 28),
        op((810, 550, 960, 640), (832, 575), "proof", BLACK, 28),
        op((990, 550, 1145, 640), (1010, 575), "lesson", BLACK, 28),
        op((1125, 175, 1295, 345), (1145, 205), "pull direct", BLUE, 32),
    ],
    "09-common-pits-no-title.png": [
        cover((165, 245, 310, 340)),
        cover((365, 215, 625, 370)),
        cover((500, 365, 600, 455)),
        cover((505, 455, 625, 535)),
        cover((505, 545, 615, 625)),
        cover((680, 215, 965, 370)),
        cover((830, 500, 955, 585)),
        cover((850, 585, 970, 675)),
        cover((845, 675, 980, 760)),
        cover((995, 215, 1390, 380)),
        cover((1220, 410, 1360, 545)),
        cover((1470, 380, 1630, 520)),
        op((180, 260, 285, 315), (192, 270), "start", RED, 24),
        op((390, 230, 520, 290), (402, 242), "overload", RED, 24),
        op((690, 230, 830, 290), (702, 242), "no proof", RED, 24),
        op((1010, 230, 1170, 290), (1022, 242), "fake clarity", RED, 24),
        op((1290, 405, 1445, 465), (1302, 417), "wrong turn", BLUE, 24),
        op((500, 385, 610, 445), (512, 398), "hot topic", BLACK, 24),
        op((835, 520, 950, 580), (848, 532), "content", BLACK, 24),
        op((1228, 430, 1350, 490), (1240, 442), "AI draft", BLACK, 24),
        op((1485, 405, 1620, 485), (1498, 425), "do not\nstare", BLUE, 24),
    ],
    "13-system-bearing.png": [
        cover((120, 505, 330, 710)),
        cover((350, 150, 565, 710)),
        cover((1055, 285, 1445, 480)),
        cover((1130, 245, 1620, 385)),
        cover((1410, 195, 1645, 320)),
        cover((1080, 330, 1445, 420)),
        cover((890, 485, 1135, 680)),
        cover((1210, 495, 1385, 620)),
        cover((1240, 620, 1515, 800)),
        op((130, 520, 315, 690), (182, 585), "load", RED, 28),
        op((360, 170, 545, 690), (390, 210), "repeat\nrepeat\nrepeat\nrepeat\nrepeat\nrepeat\nrepeat", BLACK, 28),
        op((1070, 300, 1425, 465), (1105, 330), "repeat repeat repeat\nrepeat repeat repeat", BLACK, 28),
        op((1145, 255, 1600, 365), (1192, 292), "system load", ORANGE, 32),
        op((1095, 330, 1400, 435), (1110, 360), "repeat repeat repeat", BLACK, 28),
        op((910, 500, 1115, 660), (965, 555), "loose", ORANGE, 32),
        op((1230, 510, 1365, 600), (1244, 536), "judge", BLACK, 24),
        op((1260, 635, 1495, 780), (1290, 690), "only judgment", BLUE, 32),
        op((1120, 700, 1270, 760), (1132, 712), "support", BLUE, 24),
    ],
}


ALIASES = {
    "03-sort-by-purpose.png": "02-sort-by-purpose.png",
    "04-one-fish-many-uses.png": "03-one-fish-many-uses.png",
    "05-handoff-path.png": "04-handoff-path.png",
    "10-information-well.png": "05-information-well.png",
    "11-idea-press.png": "06-idea-press.png",
    "12-content-fermentation.png": "07-content-fermentation.png",
    "14-trust-bridge.png": "08-trust-bridge.png",
}


def ops_for(path):
    key = ALIASES.get(path.name, path.name)
    return OPS.get(key, [])


def main():
    paths = sorted(Path("examples/images").glob("*.png"))
    paths += sorted(Path("ian-xiaohei-illustrations/assets/examples").glob("*.png"))
    missing = []
    for path in paths:
        ops = ops_for(path)
        if not ops:
            missing.append(str(path))
            continue
        apply_ops(path, ops)
    if missing:
        raise SystemExit("missing operations for: " + ", ".join(missing))


if __name__ == "__main__":
    main()
