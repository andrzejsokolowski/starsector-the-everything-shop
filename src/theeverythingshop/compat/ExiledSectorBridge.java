package theeverythingshop.compat;

import com.fs.starfarer.api.campaign.SpecialItemData;
import exiledsector.items.ItemData;
import exiledsector.items.ItemDefinition;
import exiledsector.items.ItemDefinitions;
import exiledsector.items.ItemType;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * The only class that touches Exiled Sector's code. Only {@link ExiledSectorCompat} calls it,
 * after checking the mod is enabled, and it catches the LinkageError a different version throws.
 *
 * Items are rolled by Exiled Sector itself, the same way its loot is, so every item on the shelf
 * is one the mod recognises. Each entry is {item id, data}.
 */
final class ExiledSectorBridge {

    private ExiledSectorBridge() {
    }

    /** One rolled item per hull item and per subroutine. */
    static List<String[]> hullItems(Random random) {
        List<String[]> out = new ArrayList<String[]>();
        for (ItemType type : new ItemType[] { ItemType.HULL_ITEM, ItemType.SUBROUTINE }) {
            for (ItemDefinition def : ItemDefinitions.ofType(type)) {
                add(out, ItemData.rolled(def, random.nextLong()));
            }
        }
        return out;
    }

    /** One star chart of every kind at every tier. */
    static List<String[]> starCharts(Random random, int maxTier) {
        List<String[]> out = new ArrayList<String[]>();
        for (ItemDefinition def : ItemDefinitions.ofType(ItemType.STAR_CHART)) {
            for (int tier = 1; tier <= maxTier; tier++) {
                add(out, ItemData.rolledAtTier(def, random.nextLong(), tier));
            }
        }
        return out;
    }

    private static void add(List<String[]> out, ItemData data) {
        if (data == null || data.preview() == null) {
            return; // Exiled Sector can't show it: it would be an "Unrecognised hull item"
        }
        SpecialItemData item = data.toSpecialItem();
        if (item != null && item.getId() != null && item.getData() != null) {
            out.add(new String[] { item.getId(), item.getData() });
        }
    }
}
