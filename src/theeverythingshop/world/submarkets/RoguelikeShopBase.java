package theeverythingshop.world.submarkets;

import com.fs.starfarer.api.Global;
import com.fs.starfarer.api.campaign.CargoAPI;
import com.fs.starfarer.api.campaign.SpecialItemSpecAPI;
import theeverythingshop.compat.ExiledSectorCompat;
import theeverythingshop.items.DataItemStock;
import theeverythingshop.items.SpecialItemRules;

/**
 * The shops on the RogueLike Shop station: Exiled Sector's items, one kind per shop, 999 of
 * each. Same prices, restock and no-selling rules as The Treasury. Hull items and star charts
 * are rolled by Exiled Sector itself, so each restock brings new rolls.
 */
public abstract class RoguelikeShopBase extends TreasuryShopBase {

    public enum Kind { CONSUMABLES, STAR_CHARTS, HULL_ITEMS, NANOSWARMS, ENGRAMS, CIPHERS }

    protected abstract Kind kind();

    @Override
    protected void addStock(CargoAPI cargo) {
        if (!ExiledSectorCompat.isAvailable()) {
            return;
        }
        switch (kind()) {
            case HULL_ITEMS:
                for (String[] entry : ExiledSectorCompat.hullItems()) {
                    addSpecial(cargo, entry[0], entry[1], STOCK);
                }
                return;
            case STAR_CHARTS:
                for (String[] entry : ExiledSectorCompat.starCharts()) {
                    addSpecial(cargo, entry[0], entry[1], STOCK);
                }
                return;
            case CONSUMABLES:
                for (String[] entry : DataItemStock.exiledSchematics(STOCK)) {
                    addSpecial(cargo, entry[0], entry[1], Integer.parseInt(entry[2]));
                }
                break;
            default:
                break;
        }
        for (SpecialItemSpecAPI spec : Global.getSettings().getAllSpecialItemSpecs()) {
            String id = spec.getId();
            if (id == null || !id.startsWith(ExiledSectorCompat.ITEM_PREFIX) || kindOf(id) != kind()
                    || !SpecialItemRules.isPlainShopItem(spec)) {
                continue;
            }
            addSpecial(cargo, id, null, STOCK);
        }
    }

    /** Which shop a plain Exiled Sector item belongs in. */
    public static Kind kindOf(String id) {
        if (id.contains("nanoswarm") || id.contains("nanoseed") || id.contains("nanite_feedstock")) {
            return Kind.NANOSWARMS;
        }
        if (id.endsWith("_engram")) {
            return Kind.ENGRAMS;
        }
        if (id.endsWith("_cipher")) {
            return Kind.CIPHERS;
        }
        return Kind.CONSUMABLES;
    }
}
