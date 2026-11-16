package theeverythingshop.world.submarkets;

import com.fs.starfarer.api.campaign.CargoAPI;
import com.fs.starfarer.api.campaign.SpecialItemData;
import theeverythingshop.compat.ExoticaCompat;

/**
 * Exotics (Exotica Technologies only): every exotic chip in every form (normal, corrupted,
 * pure and the fork's guerilla). Exotics that install from an AI core get no chip.
 * Exotica Upgrades extends this shop, so both cost ten times the Treasury price.
 */
public class TreasuryExotics extends TreasuryShopBase {

    @Override
    protected void addStock(CargoAPI cargo) {
        for (String[] entry : ExoticaCompat.listExotics()) {
            addSafely(cargo, entry[0], entry[1]);
        }
    }

    protected void addSafely(CargoAPI cargo, String id, String data) {
        try {
            cargo.addSpecial(new SpecialItemData(id, data), STOCK);
        } catch (Throwable t) {
            log.warn("Skipping Exotica item " + id + " " + data, t);
            cargo.removeEmptyStacks();
        }
    }

    /** Exotica chips are worth little because the mod never sells them; here they cost ten times as much. */
    public static final float PRICE_MULT = 10f;

    // The buy price is the item's price times (1 + tariff), so this makes it ten times the Treasury price
    @Override
    public float getTariff() {
        return (1f + super.getTariff()) * PRICE_MULT - 1f;
    }

    @Override
    protected String getDisplayName() {
        return "Exotica\nExotics";
    }
}
