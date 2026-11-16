package theeverythingshop.world.submarkets;

/** RogueLike Shop: Exiled Sector hull items. */
public class RoguelikeHullItems extends RoguelikeShopBase {

    @Override
    protected Kind kind() {
        return Kind.HULL_ITEMS;
    }

    @Override
    protected String getDisplayName() {
        return "Hull\nItems";
    }
}