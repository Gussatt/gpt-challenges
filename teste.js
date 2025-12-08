function findLowestPrice(products, discounts) {
    let total = 0;

    for (let i = 0; i < products.length; i++) {
        const basePrice = Number(products[i][0]);
        let lowest = basePrice;

        for (let j = 1; j < products[i].length; j++) {
            const productDiscountTag = products[i][j];

            if (productDiscountTag === 'EMPTY') continue;

            for (let z = 0; z < discounts.length; z++) {
                if (discounts[z][0] === productDiscountTag) {
                    const discountType = Number(discounts[z][1]);
                    const discountValue = Number(discounts[z][2]);
                    let price = basePrice;

                    switch (discountType) {
                        case 0: // fixed price
                            price = discountValue;
                            break;
                        case 1: // percentage
                            price = basePrice - (discountValue / 100 * basePrice);
                            break;
                        case 2: // subtract amount
                            price = basePrice - discountValue;
                            break;
                    }

                    if (price < lowest) {
                        lowest = price;
                    }
                }
            }
        }

        total += lowest;
    }

    console.log(total);
}

const products = [['10','sale','january-sale'],['20','sale','EMPTY']];
const discounts = [['sale', '0', '10'], ['january-sale', '1', '27'], ['sales', '2', '27']];

findLowestPrice(products, discounts); // Output: 22.7
