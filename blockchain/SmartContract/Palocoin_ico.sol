pragma solidity 0.4.24;
contract palocoin_ico {
    // Introducing the maximum number of Palocoin available for sale
    uint public max_palocoins = 1000000;

    // Introducing the EUR to Palocoin conversion rate
    uint public eur_to_palocoins = 1000;

    //Introducing the total number of Palocoin that have been bought by inverstors
    uint public total_palocoins_bought = 0;

    //Mapping from the inverstors address to its equity in Palocoin and EUR
    mapping(address => uint) equity_palocoins;
    mapping(address => uint) equity_eur;

    //Checking if an investor can buy Palocoin
    modifier can_buy_Palocoins(uint eur_invested) {
        require (eur_invested * eur_to_palocoins + total_palocoins_bought <= max_palocoins);
        _;
    }
    // Getting the equity in Palocoin of an investor
    function equity_in_palocoins(address inverstor) external constant return(uint)

}