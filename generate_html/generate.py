import os
prefix='''<!DOCTYPE html>
<html>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width">
<link rel="stylesheet" type="text/css" media="all" href="css/index_styles.css">
<link rel="stylesheet" type="text/css" media="all" href="css/treeFrame_styles.css">

<script src="https://cdn.bootcss.com/jquery/1.12.4/jquery.min.js">
</script>
<title>Nav</title>
<script>
    function searchItem() {
        var ItemList = $(".index_itembox");
        var searchColumn = $('input#searchColumnInput');
        var searchKey = searchColumn.val();
        console.log(ItemList.length);
        var count = 0;
        for (var i = 0; i < ItemList.length; i++) {
            if (String($(ItemList.get(i)).text()).indexOf(String(searchKey)) >= 0) {
                $(ItemList.get(i)).show();
                count += 1;
            } else {
                $(ItemList.get(i)).hide();
            }
            $("div.floatWarning").text("found " + count + " results");
            window.parent.changeiFrameHeight();
        }
    }
</script>

<body>
    <div class="searchDiv">
        <div class="searchColumnDiv">
            <input onkeyup="searchItem()" id="searchColumnInput" placeholder="search  article">
            <?php
                echo "test";
                ?>
                </input>
        </div>
        <div class="floatWarning">
        </div>
    </div>
    <div class="index_list">'''
suffix='''    </div>
</body>

</html>'''



print prefix
L=os.listdir("../ARTICLE")
L.sort()
L.reverse()
for each in L:
    if each.endswith(".html"):
        print '<div class="index_itembox">\n' \
              '<a class="index_item" href="javascript:window.parent.switchDisplayPage(\'ARTICLE/%s\')">' \
              '%s</a><br>\n</div>'%(each,each.replace("_"," ").strip(".html"))
print suffix