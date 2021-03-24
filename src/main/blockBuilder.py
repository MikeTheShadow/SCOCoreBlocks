from shutil import copyfile
import sys
import os.path
from os import path


def edit_lang(block_id, block_name):
    lang_file = open("resources/assets/scocoreblocks/lang/en_us.json", "r")
    body = lang_file.read()
    lang_file.close()
    lang_file = open("resources/assets/scocoreblocks/lang/en_us.json", "w")
    body = body.replace("}", "\t,\"block.scocoreblocks." + block_id + "\": \"" + block_name + "\"" + "\n}");
    lang_file.write(body)


def create_file(template, location, block_id):
    file = open(template, 'r')
    text = file.read()
    file.close()
    while "firstblock" in text:
        text = text.replace("firstblock", block_id)
    file = open(location + block_id + ".json", 'w')
    file.write(text)
    file.close()


def modify_main_class(class_name, block_id, var_name):
    file = open("java/com/miketheshadow/scocoreblocks/SCOCoreBlocks.java", 'r')
    text = file.read()
    file.close()
    # First replace //block-reg
    rep = "event.getRegistry().register(new " + class_name + "());"
    text = text.replace("//block-reg", "//block-reg\n\t\t\t" + rep)

    rep = "event.getRegistry().register(new BlockItem(ModBlocks." + var_name + ", properties).setRegistryName(\"" \
          + block_id + "\"));"
    text = text.replace("//item-reg", "//item-reg\n\t\t\t" + rep)

    file = open("java/com/miketheshadow/scocoreblocks/SCOCoreBlocks.java", 'w')
    file.write(text)
    file.close()


def add_block_to_blocks(class_name, block_id):
    file = open("java/com/miketheshadow/scocoreblocks/ModBlocks.java", 'r')
    text = file.read()
    var_name = class_name.replace(class_name[0], class_name[0].lower())
    addition = "\t@ObjectHolder(\"scocoreblocks:" \
               + block_id + "\")\n\tpublic static " \
               + class_name \
               + " " + var_name + ";"
    text = text.replace("//replace", "//replace\n" + addition)
    file = open("java/com/miketheshadow/scocoreblocks/ModBlocks.java", 'w')
    file.write(text)
    modify_main_class(class_name, block_id,var_name)


def create_java_file(block_name, block_id):
    while " " in block_name:
        block_name = block_name.replace(" ", "")
    file = open("templates/block.java", 'r')
    text = file.read()
    file.close()
    while "FirstBlock" in text:
        text = text.replace("FirstBlock", block_name)
    text = text.replace("firstblock", block_id)
    file = open("java/com/miketheshadow/scocoreblocks/blocks/" + block_name + ".java", 'w')
    file.write(text)
    file.close()
    add_block_to_blocks(block_name, block_id)


def main():
    if len(sys.argv) != 3:
        for s in sys.argv:
            print(s)
        print("length: " + str(len(sys.argv)))
        print("missing argument for block id or name")
        print("ex: blockBuilder.py block_id blockName")
        return

    block_id = sys.argv[1]
    block_name = sys.argv[2]

    if not path.exists(block_id + ".png"):
        print("Error block with id " + block_id + " does not exist!")
        return
    while "-" in block_name:
        block_name = block_name.replace("-", " ")
    if True:
        assets = "resources/assets/scocoreblocks/"
        # Add lang
        print("Editing lang...")
        edit_lang(block_id, block_name)
        # Edit block state
        print("Editing state...")
        create_file("templates/blockstates.json", assets + "blockstates/", block_id)
        # Edit model block
        print("Editing models/block...")
        create_file("templates/model_block.json", assets + "models/block/", block_id)
        # Edit model item
        print("Editing mdoels/item...")
        create_file("templates/model_item.json", assets + "models/item/", block_id)
        # Add block texture
        print("Copying file...")
        copyfile(block_id + ".png", assets + "textures/block/" + block_id + ".png")
        # Create block class and add to ModBlocks
        print("Creating block class...")
        create_java_file(block_name, block_id)

        print("Complete!")


if __name__ == "__main__":
    main()
