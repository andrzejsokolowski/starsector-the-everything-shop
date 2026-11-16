package theeverythingshop.world.submarkets;

/** RogueLike Shop: Exiled Sector consumables. */
public class RoguelikeConsumables extends RoguelikeShopBase {

    @Override
    protected Kind kind() {
        return Kind.CONSUMABLES;
    }

    @Override
    protected String getDisplayName() {
        return "Consumables";
    }
}