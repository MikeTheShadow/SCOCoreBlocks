package com.miketheshadow.scocoreblocks.setup;

import com.miketheshadow.scocoreblocks.ModBlocks;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;

public class ModSetup {

    public static ItemGroup itemGroup = new ItemGroup("scocoreblocks") {
        @Override
        public ItemStack createIcon() {
            return new ItemStack(ModBlocks.firstBlock);
        }
    };

    public void init() {

    }

}
