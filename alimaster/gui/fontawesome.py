#
# alimsater/gui/fontawesome.py
#
# flake8: noqa
#
"""
Tools for using the FontAwesome in ttk applications
"""

from alimaster import RES

from PIL import ImageFont


def get_font(size):
    return ImageFont.truetype(RES("fontawesome.ttf"), size)

_font = get_font(1000)
_font_16 = get_font(16)


ICONS = {     "adjust" : "\uf042",
                 "adn" : "\uf170",
        "align-center" : "\uf037",
       "align-justify" : "\uf039",
          "align-left" : "\uf036",
         "align-right" : "\uf038",
           "ambulance" : "\uf0f9",
              "anchor" : "\uf13d",
             "android" : "\uf17b",
           "angellist" : "\uf209",
   "angle-double-down" : "\uf103",
   "angle-double-left" : "\uf100",
  "angle-double-right" : "\uf101",
     "angle-double-up" : "\uf102",
          "angle-down" : "\uf107",
          "angle-left" : "\uf104",
         "angle-right" : "\uf105",
            "angle-up" : "\uf106",
               "apple" : "\uf179",
             "archive" : "\uf187",
          "area-chart" : "\uf1fe",
   "arrow-circle-down" : "\uf0ab",
   "arrow-circle-left" : "\uf0a8",
 "arrow-circle-o-down" : "\uf01a",
 "arrow-circle-o-left" : "\uf190",
"arrow-circle-o-right" : "\uf18e",
   "arrow-circle-o-up" : "\uf01b",
  "arrow-circle-right" : "\uf0a9",
     "arrow-circle-up" : "\uf0aa",
          "arrow-down" : "\uf063",
          "arrow-left" : "\uf060",
         "arrow-right" : "\uf061",
            "arrow-up" : "\uf062",
              "arrows" : "\uf047",
          "arrows-alt" : "\uf0b2",
            "arrows-h" : "\uf07e",
            "arrows-v" : "\uf07d",
            "asterisk" : "\uf069",
                  "at" : "\uf1fa",
          "automobile" : "\uf1b9",
            "backward" : "\uf04a",
                 "ban" : "\uf05e",
                "bank" : "\uf19c",
           "bar-chart" : "\uf080",
         "bar-chart-o" : "\uf080",
             "barcode" : "\uf02a",
                "bars" : "\uf0c9",
                 "bed" : "\uf236",
                "beer" : "\uf0fc",
             "behance" : "\uf1b4",
      "behance-square" : "\uf1b5",
                "bell" : "\uf0f3",
              "bell-o" : "\uf0a2",
          "bell-slash" : "\uf1f6",
        "bell-slash-o" : "\uf1f7",
             "bicycle" : "\uf206",
          "binoculars" : "\uf1e5",
       "birthday-cake" : "\uf1fd",
           "bitbucket" : "\uf171",
    "bitbucket-square" : "\uf172",
             "bitcoin" : "\uf15a",
                "bold" : "\uf032",
                "bolt" : "\uf0e7",
                "bomb" : "\uf1e2",
                "book" : "\uf02d",
            "bookmark" : "\uf02e",
          "bookmark-o" : "\uf097",
           "briefcase" : "\uf0b1",
                 "btc" : "\uf15a",
                 "bug" : "\uf188",
            "building" : "\uf1ad",
          "building-o" : "\uf0f7",
            "bullhorn" : "\uf0a1",
            "bullseye" : "\uf140",
                 "bus" : "\uf207",
          "buysellads" : "\uf20d",
                 "cab" : "\uf1ba",
          "calculator" : "\uf1ec",
            "calendar" : "\uf073",
          "calendar-o" : "\uf133",
              "camera" : "\uf030",
        "camera-retro" : "\uf083",
                 "car" : "\uf1b9",
          "caret-down" : "\uf0d7",
          "caret-left" : "\uf0d9",
         "caret-right" : "\uf0da",
 "caret-square-o-down" : "\uf150",
 "caret-square-o-left" : "\uf191",
"caret-square-o-right" : "\uf152",
   "caret-square-o-up" : "\uf151",
            "caret-up" : "\uf0d8",
     "cart-arrow-down" : "\uf218",
           "cart-plus" : "\uf217",
                  "cc" : "\uf20a",
             "cc-amex" : "\uf1f3",
         "cc-discover" : "\uf1f2",
       "cc-mastercard" : "\uf1f1",
           "cc-paypal" : "\uf1f4",
           "cc-stripe" : "\uf1f5",
             "cc-visa" : "\uf1f0",
         "certificate" : "\uf0a3",
               "chain" : "\uf0c1",
        "chain-broken" : "\uf127",
               "check" : "\uf00c",
        "check-circle" : "\uf058",
      "check-circle-o" : "\uf05d",
        "check-square" : "\uf14a",
      "check-square-o" : "\uf046",
 "chevron-circle-down" : "\uf13a",
 "chevron-circle-left" : "\uf137",
"chevron-circle-right" : "\uf138",
   "chevron-circle-up" : "\uf139",
        "chevron-down" : "\uf078",
        "chevron-left" : "\uf053",
       "chevron-right" : "\uf054",
          "chevron-up" : "\uf077",
               "child" : "\uf1ae",
              "circle" : "\uf111",
            "circle-o" : "\uf10c",
      "circle-o-notch" : "\uf1ce",
         "circle-thin" : "\uf1db",
           "clipboard" : "\uf0ea",
             "clock-o" : "\uf017",
               "close" : "\uf00d",
               "cloud" : "\uf0c2",
      "cloud-download" : "\uf0ed",
        "cloud-upload" : "\uf0ee",
                 "cny" : "\uf157",
                "code" : "\uf121",
           "code-fork" : "\uf126",
             "codepen" : "\uf1cb",
              "coffee" : "\uf0f4",
                 "cog" : "\uf013",
                "cogs" : "\uf085",
             "columns" : "\uf0db",
             "comment" : "\uf075",
           "comment-o" : "\uf0e5",
            "comments" : "\uf086",
          "comments-o" : "\uf0e6",
             "compass" : "\uf14e",
            "compress" : "\uf066",
      "connectdevelop" : "\uf20e",
                "copy" : "\uf0c5",
           "copyright" : "\uf1f9",
         "credit-card" : "\uf09d",
                "crop" : "\uf125",
          "crosshairs" : "\uf05b",
                "cube" : "\uf1b2",
               "cubes" : "\uf1b3",
                 "cut" : "\uf0c4",
             "cutlery" : "\uf0f5",
           "dashboard" : "\uf0e4",
            "dashcube" : "\uf210",
            "database" : "\uf1c0",
              "dedent" : "\uf03b",
           "delicious" : "\uf1a5",
             "desktop" : "\uf108",
          "deviantart" : "\uf1bd",
             "diamond" : "\uf219",
                "digg" : "\uf1a6",
              "dollar" : "\uf155",
        "dot-circle-o" : "\uf192",
            "download" : "\uf019",
            "dribbble" : "\uf17d",
             "dropbox" : "\uf16b",
              "drupal" : "\uf1a9",
                "edit" : "\uf044",
               "eject" : "\uf052",
          "ellipsis-h" : "\uf141",
          "ellipsis-v" : "\uf142",
              "empire" : "\uf1d1",
            "envelope" : "\uf0e0",
          "envelope-o" : "\uf003",
     "envelope-square" : "\uf199",
              "eraser" : "\uf12d",
                 "eur" : "\uf153",
                "euro" : "\uf153",
            "exchange" : "\uf0ec",
         "exclamation" : "\uf12a",
  "exclamation-circle" : "\uf06a",
"exclamation-triangle" : "\uf071",
              "expand" : "\uf065",
       "external-link" : "\uf08e",
"external-link-square" : "\uf14c",
                 "eye" : "\uf06e",
           "eye-slash" : "\uf070",
          "eyedropper" : "\uf1fb",
            "facebook" : "\uf09a",
          "facebook-f" : "\uf09a",
   "facebook-official" : "\uf230",
     "facebook-square" : "\uf082",
       "fast-backward" : "\uf049",
        "fast-forward" : "\uf050",
                 "fax" : "\uf1ac",
              "female" : "\uf182",
         "fighter-jet" : "\uf0fb",
                "file" : "\uf15b",
      "file-archive-o" : "\uf1c6",
        "file-audio-o" : "\uf1c7",
         "file-code-o" : "\uf1c9",
        "file-excel-o" : "\uf1c3",
        "file-image-o" : "\uf1c5",
        "file-movie-o" : "\uf1c8",
              "file-o" : "\uf016",
          "file-pdf-o" : "\uf1c1",
        "file-photo-o" : "\uf1c5",
      "file-picture-o" : "\uf1c5",
   "file-powerpoint-o" : "\uf1c4",
        "file-sound-o" : "\uf1c7",
           "file-text" : "\uf15c",
         "file-text-o" : "\uf0f6",
        "file-video-o" : "\uf1c8",
         "file-word-o" : "\uf1c2",
          "file-zip-o" : "\uf1c6",
             "files-o" : "\uf0c5",
                "film" : "\uf008",
              "filter" : "\uf0b0",
                "fire" : "\uf06d",
   "fire-extinguisher" : "\uf134",
                "flag" : "\uf024",
      "flag-checkered" : "\uf11e",
              "flag-o" : "\uf11d",
               "flash" : "\uf0e7",
               "flask" : "\uf0c3",
              "flickr" : "\uf16e",
            "floppy-o" : "\uf0c7",
              "folder" : "\uf07b",
            "folder-o" : "\uf114",
         "folder-open" : "\uf07c",
       "folder-open-o" : "\uf115",
                "font" : "\uf031",
            "forumbee" : "\uf211",
             "forward" : "\uf04e",
          "foursquare" : "\uf180",
             "frown-o" : "\uf119",
            "futbol-o" : "\uf1e3",
             "gamepad" : "\uf11b",
               "gavel" : "\uf0e3",
                 "gbp" : "\uf154",
                  "ge" : "\uf1d1",
                "gear" : "\uf013",
               "gears" : "\uf085",
          "genderless" : "\uf1db",
                "gift" : "\uf06b",
                 "git" : "\uf1d3",
          "git-square" : "\uf1d2",
              "github" : "\uf09b",
          "github-alt" : "\uf113",
       "github-square" : "\uf092",
              "gittip" : "\uf184",
               "glass" : "\uf000",
               "globe" : "\uf0ac",
              "google" : "\uf1a0",
         "google-plus" : "\uf0d5",
  "google-plus-square" : "\uf0d4",
       "google-wallet" : "\uf1ee",
      "graduation-cap" : "\uf19d",
            "gratipay" : "\uf184",
               "group" : "\uf0c0",
            "h-square" : "\uf0fd",
         "hacker-news" : "\uf1d4",
         "hand-o-down" : "\uf0a7",
         "hand-o-left" : "\uf0a5",
        "hand-o-right" : "\uf0a4",
           "hand-o-up" : "\uf0a6",
               "hdd-o" : "\uf0a0",
              "header" : "\uf1dc",
          "headphones" : "\uf025",
               "heart" : "\uf004",
             "heart-o" : "\uf08a",
           "heartbeat" : "\uf21e",
             "history" : "\uf1da",
                "home" : "\uf015",
          "hospital-o" : "\uf0f8",
               "hotel" : "\uf236",
                 "ils" : "\uf20b",
               "image" : "\uf03e",
               "inbox" : "\uf01c",
              "indent" : "\uf03c",
                "info" : "\uf129",
         "info-circle" : "\uf05a",
                 "inr" : "\uf156",
           "instagram" : "\uf16d",
         "institution" : "\uf19c",
             "ioxhost" : "\uf208",
              "italic" : "\uf033",
              "joomla" : "\uf1aa",
                 "jpy" : "\uf157",
            "jsfiddle" : "\uf1cc",
                 "key" : "\uf084",
          "keyboard-o" : "\uf11c",
                 "krw" : "\uf159",
            "language" : "\uf1ab",
              "laptop" : "\uf109",
              "lastfm" : "\uf202",
       "lastfm-square" : "\uf203",
                "leaf" : "\uf06c",
             "leanpub" : "\uf212",
               "legal" : "\uf0e3",
             "lemon-o" : "\uf094",
          "level-down" : "\uf149",
            "level-up" : "\uf148",
           "life-bouy" : "\uf1cd",
           "life-buoy" : "\uf1cd",
           "life-ring" : "\uf1cd",
          "life-saver" : "\uf1cd",
         "lightbulb-o" : "\uf0eb",
          "line-chart" : "\uf201",
                "link" : "\uf0c1",
            "linkedin" : "\uf0e1",
     "linkedin-square" : "\uf08c",
               "linux" : "\uf17c",
                "list" : "\uf03a",
            "list-alt" : "\uf022",
             "list-ol" : "\uf0cb",
             "list-ul" : "\uf0ca",
      "location-arrow" : "\uf124",
                "lock" : "\uf023",
     "long-arrow-down" : "\uf175",
     "long-arrow-left" : "\uf177",
    "long-arrow-right" : "\uf178",
       "long-arrow-up" : "\uf176",
               "magic" : "\uf0d0",
              "magnet" : "\uf076",
        "mail-forward" : "\uf064",
          "mail-reply" : "\uf112",
      "mail-reply-all" : "\uf122",
                "male" : "\uf183",
          "map-marker" : "\uf041",
                "mars" : "\uf222",
         "mars-double" : "\uf227",
         "mars-stroke" : "\uf229",
       "mars-stroke-h" : "\uf22b",
       "mars-stroke-v" : "\uf22a",
              "maxcdn" : "\uf136",
            "meanpath" : "\uf20c",
              "medium" : "\uf23a",
              "medkit" : "\uf0fa",
               "meh-o" : "\uf11a",
             "mercury" : "\uf223",
          "microphone" : "\uf130",
    "microphone-slash" : "\uf131",
               "minus" : "\uf068",
        "minus-circle" : "\uf056",
        "minus-square" : "\uf146",
      "minus-square-o" : "\uf147",
              "mobile" : "\uf10b",
        "mobile-phone" : "\uf10b",
               "money" : "\uf0d6",
              "moon-o" : "\uf186",
        "mortar-board" : "\uf19d",
          "motorcycle" : "\uf21c",
               "music" : "\uf001",
             "navicon" : "\uf0c9",
              "neuter" : "\uf22c",
         "newspaper-o" : "\uf1ea",
              "openid" : "\uf19b",
             "outdent" : "\uf03b",
           "pagelines" : "\uf18c",
         "paint-brush" : "\uf1fc",
         "paper-plane" : "\uf1d8",
       "paper-plane-o" : "\uf1d9",
           "paperclip" : "\uf0c6",
           "paragraph" : "\uf1dd",
               "paste" : "\uf0ea",
               "pause" : "\uf04c",
                 "paw" : "\uf1b0",
              "paypal" : "\uf1ed",
              "pencil" : "\uf040",
       "pencil-square" : "\uf14b",
     "pencil-square-o" : "\uf044",
               "phone" : "\uf095",
        "phone-square" : "\uf098",
               "photo" : "\uf03e",
           "picture-o" : "\uf03e",
           "pie-chart" : "\uf200",
          "pied-piper" : "\uf1a7",
      "pied-piper-alt" : "\uf1a8",
           "pinterest" : "\uf0d2",
         "pinterest-p" : "\uf231",
    "pinterest-square" : "\uf0d3",
               "plane" : "\uf072",
                "play" : "\uf04b",
         "play-circle" : "\uf144",
       "play-circle-o" : "\uf01d",
                "plug" : "\uf1e6",
                "plus" : "\uf067",
         "plus-circle" : "\uf055",
         "plus-square" : "\uf0fe",
       "plus-square-o" : "\uf196",
           "power-off" : "\uf011",
               "print" : "\uf02f",
        "puzzle-piece" : "\uf12e",
                  "qq" : "\uf1d6",
              "qrcode" : "\uf029",
            "question" : "\uf128",
     "question-circle" : "\uf059",
          "quote-left" : "\uf10d",
         "quote-right" : "\uf10e",
                  "ra" : "\uf1d0",
              "random" : "\uf074",
               "rebel" : "\uf1d0",
             "recycle" : "\uf1b8",
              "reddit" : "\uf1a1",
       "reddit-square" : "\uf1a2",
             "refresh" : "\uf021",
              "remove" : "\uf00d",
              "renren" : "\uf18b",
             "reorder" : "\uf0c9",
              "repeat" : "\uf01e",
               "reply" : "\uf112",
           "reply-all" : "\uf122",
             "retweet" : "\uf079",
                 "rmb" : "\uf157",
                "road" : "\uf018",
              "rocket" : "\uf135",
         "rotate-left" : "\uf0e2",
        "rotate-right" : "\uf01e",
              "rouble" : "\uf158",
                 "rss" : "\uf09e",
          "rss-square" : "\uf143",
                 "rub" : "\uf158",
               "ruble" : "\uf158",
               "rupee" : "\uf156",
                "save" : "\uf0c7",
            "scissors" : "\uf0c4",
              "search" : "\uf002",
        "search-minus" : "\uf010",
         "search-plus" : "\uf00e",
              "sellsy" : "\uf213",
                "send" : "\uf1d8",
              "send-o" : "\uf1d9",
              "server" : "\uf233",
               "share" : "\uf064",
           "share-alt" : "\uf1e0",
    "share-alt-square" : "\uf1e1",
        "share-square" : "\uf14d",
      "share-square-o" : "\uf045",
              "shekel" : "\uf20b",
              "sheqel" : "\uf20b",
              "shield" : "\uf132",
                "ship" : "\uf21a",
        "shirtsinbulk" : "\uf214",
       "shopping-cart" : "\uf07a",
             "sign-in" : "\uf090",
            "sign-out" : "\uf08b",
              "signal" : "\uf012",
         "simplybuilt" : "\uf215",
             "sitemap" : "\uf0e8",
            "skyatlas" : "\uf216",
               "skype" : "\uf17e",
               "slack" : "\uf198",
             "sliders" : "\uf1de",
          "slideshare" : "\uf1e7",
             "smile-o" : "\uf118",
       "soccer-ball-o" : "\uf1e3",
                "sort" : "\uf0dc",
      "sort-alpha-asc" : "\uf15d",
     "sort-alpha-desc" : "\uf15e",
     "sort-amount-asc" : "\uf160",
    "sort-amount-desc" : "\uf161",
            "sort-asc" : "\uf0de",
           "sort-desc" : "\uf0dd",
           "sort-down" : "\uf0dd",
    "sort-numeric-asc" : "\uf162",
   "sort-numeric-desc" : "\uf163",
             "sort-up" : "\uf0de",
          "soundcloud" : "\uf1be",
       "space-shuttle" : "\uf197",
             "spinner" : "\uf110",
               "spoon" : "\uf1b1",
             "spotify" : "\uf1bc",
              "square" : "\uf0c8",
            "square-o" : "\uf096",
      "stack-exchange" : "\uf18d",
      "stack-overflow" : "\uf16c",
                "star" : "\uf005",
           "star-half" : "\uf089",
     "star-half-empty" : "\uf123",
      "star-half-full" : "\uf123",
         "star-half-o" : "\uf123",
              "star-o" : "\uf006",
               "steam" : "\uf1b6",
        "steam-square" : "\uf1b7",
       "step-backward" : "\uf048",
        "step-forward" : "\uf051",
         "stethoscope" : "\uf0f1",
                "stop" : "\uf04d",
         "street-view" : "\uf21d",
       "strikethrough" : "\uf0cc",
         "stumbleupon" : "\uf1a4",
  "stumbleupon-circle" : "\uf1a3",
           "subscript" : "\uf12c",
              "subway" : "\uf239",
            "suitcase" : "\uf0f2",
               "sun-o" : "\uf185",
         "superscript" : "\uf12b",
             "support" : "\uf1cd",
               "table" : "\uf0ce",
              "tablet" : "\uf10a",
          "tachometer" : "\uf0e4",
                 "tag" : "\uf02b",
                "tags" : "\uf02c",
               "tasks" : "\uf0ae",
                "taxi" : "\uf1ba",
       "tencent-weibo" : "\uf1d5",
            "terminal" : "\uf120",
         "text-height" : "\uf034",
          "text-width" : "\uf035",
                  "th" : "\uf00a",
            "th-large" : "\uf009",
             "th-list" : "\uf00b",
          "thumb-tack" : "\uf08d",
         "thumbs-down" : "\uf165",
       "thumbs-o-down" : "\uf088",
         "thumbs-o-up" : "\uf087",
           "thumbs-up" : "\uf164",
              "ticket" : "\uf145",
               "times" : "\uf00d",
        "times-circle" : "\uf057",
      "times-circle-o" : "\uf05c",
                "tint" : "\uf043",
         "toggle-down" : "\uf150",
         "toggle-left" : "\uf191",
          "toggle-off" : "\uf204",
           "toggle-on" : "\uf205",
        "toggle-right" : "\uf152",
           "toggle-up" : "\uf151",
               "train" : "\uf238",
         "transgender" : "\uf224",
     "transgender-alt" : "\uf225",
               "trash" : "\uf1f8",
             "trash-o" : "\uf014",
                "tree" : "\uf1bb",
              "trello" : "\uf181",
              "trophy" : "\uf091",
               "truck" : "\uf0d1",
                 "try" : "\uf195",
                 "tty" : "\uf1e4",
              "tumblr" : "\uf173",
       "tumblr-square" : "\uf174",
        "turkish-lira" : "\uf195",
              "twitch" : "\uf1e8",
             "twitter" : "\uf099",
      "twitter-square" : "\uf081",
            "umbrella" : "\uf0e9",
           "underline" : "\uf0cd",
                "undo" : "\uf0e2",
          "university" : "\uf19c",
              "unlink" : "\uf127",
              "unlock" : "\uf09c",
          "unlock-alt" : "\uf13e",
            "unsorted" : "\uf0dc",
              "upload" : "\uf093",
                 "usd" : "\uf155",
                "user" : "\uf007",
             "user-md" : "\uf0f0",
           "user-plus" : "\uf234",
         "user-secret" : "\uf21b",
          "user-times" : "\uf235",
               "users" : "\uf0c0",
               "venus" : "\uf221",
        "venus-double" : "\uf226",
          "venus-mars" : "\uf228",
             "viacoin" : "\uf237",
        "video-camera" : "\uf03d",
        "vimeo-square" : "\uf194",
                "vine" : "\uf1ca",
                  "vk" : "\uf189",
         "volume-down" : "\uf027",
          "volume-off" : "\uf026",
           "volume-up" : "\uf028",
             "warning" : "\uf071",
              "wechat" : "\uf1d7",
               "weibo" : "\uf18a",
              "weixin" : "\uf1d7",
            "whatsapp" : "\uf232",
          "wheelchair" : "\uf193",
                "wifi" : "\uf1eb",
             "windows" : "\uf17a",
                 "won" : "\uf159",
           "wordpress" : "\uf19a",
              "wrench" : "\uf0ad",
                "xing" : "\uf168",
         "xing-square" : "\uf169",
               "yahoo" : "\uf19e",
                "yelp" : "\uf1e9",
                 "yen" : "\uf157",
             "youtube" : "\uf167",
        "youtube-play" : "\uf16a",
      "youtube-square" : "\uf166"
}


class FontAwesome:

    texture_cache = dict()

    def __init__(self):
        pass

    @classmethod
    def get_image(cls, name):
        from PIL import (Image, ImageDraw)
        if name not in cls.texture_cache:
            img = Image.new("RGBA", (1000, 1000))
            try:
                ImageDraw.Draw(img).text(
                    (0, 0),
                    ICONS[name],
                    (0, 0, 0),
                    font=_font)
            except NameError as e:
                import sys
                err_str = "Error: Could not find icon with name '%s'." % name
                print(err_str, file=sys.stderr)
                raise e
        else:
            img = cls.texture_cache[name]
        return img

    @classmethod
    def generate_icon(cls, name, size):
        from PIL import (Image)
        img = cls.get_image(name)
        return img.resize((size, size), Image.ANTIALIAS)

    @classmethod
    def get_font(cls, size):
        return get_font(size)


def _parse_cheatsheet():
    """Downloads the cheatsheet"""
    from urllib.request import urlopen
    import re
    font_awesome_url = "http://fortawesome.github.io/Font-Awesome/cheatsheet"
    html = urlopen(font_awesome_url).read().decode()
    regex = 'fa-([a-z\-]+)\s*(?:<span class="text-muted">\(alias\)</span>)?\s*<span class="muted">\s*\[&amp;#x([a-z0-9]+);\]'
    pairs = ['{0:>22} : "\\u{1}"'.format('"%s"' % x[0], x[1])
             for x in re.findall(regex, html)]
    return ',\n'.join(pairs)

if __name__ == '__main__':
    print(_parse_cheatsheet())
