package com.miketheshadow.scocoreblocks;

import com.miketheshadow.scocoreblocks.blocks.BlockOfCobalt;
import com.miketheshadow.scocoreblocks.blocks.FirstBlock;
import com.miketheshadow.scocoreblocks.blocks.MudBrick;
import net.minecraftforge.registries.ObjectHolder;

public class ModBlocks {
    //replace
	@ObjectHolder("scocoreblocks:mud_brick")
	public static MudBrick mudBrick;
	@ObjectHolder("scocoreblocks:block_cobalt")
	public static BlockOfCobalt blockOfCobalt;
    @ObjectHolder("scocoreblocks:firstblock")
    public static FirstBlock firstBlock;
}
