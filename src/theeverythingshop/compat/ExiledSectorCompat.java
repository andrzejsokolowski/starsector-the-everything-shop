package theeverythingshop.compat;

import com.fs.starfarer.api.Global;
import org.apache.log4j.Logger;

import java.util.Collections;
import java.util.List;
import java.util.Random;

/**
 * Safe access to Exiled Sector. Without the mod, or with a version whose code differs from what
 * {@link ExiledSectorBridge} expects, everything here answers "nothing" instead of crashing.
 */
public final class ExiledSectorCompat {

    public static final Logger log = Global.getLogger(ExiledSectorCompat.class);
    public static final String MOD_ID = "exiledSector";
    public static final String ITEM_PREFIX = "exiledSector_";

    /** Star chart tiers in Exiled Sector 0.12 (star_chart_tiers.csv). Higher tiers are clamped by the mod. */
    private static final int STAR_CHART_TIERS = 16;

    private ExiledSectorCompat() {
    }

    public static boolean isAvailable() {
        try {
            return Global.getSettings().getModManager().isModEnabled(MOD_ID);
        } catch (Throwable t) {
            return false;
        }
    }

    /** Hull items and subroutines, one fresh roll of each, {id, data}. */
    public static List<String[]> hullItems() {
        if (!isAvailable()) {
            return Collections.emptyList();
        }
        try {
            return ExiledSectorBridge.hullItems(new Random());
        } catch (LinkageError e) {
            log.warn("Exiled Sector version not compatible, no hull items stocked", e);
        } catch (RuntimeException e) {
            log.warn("Could not roll Exiled Sector hull items", e);
        }
        return Collections.emptyList();
    }

    /** Star charts of every tier, {id, data}. */
    public static List<String[]> starCharts() {
        if (!isAvailable()) {
            return Collections.emptyList();
        }
        try {
            return ExiledSectorBridge.starCharts(new Random(), STAR_CHART_TIERS);
        } catch (LinkageError e) {
            log.warn("Exiled Sector version not compatible, no star charts stocked", e);
        } catch (RuntimeException e) {
            log.warn("Could not roll Exiled Sector star charts", e);
        }
        return Collections.emptyList();
    }
}
