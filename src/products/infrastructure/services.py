from abc import ABC, abstractmethod

from src.products.domain.services import DiscountFetcher
from src.products.domain.value_objects import ProductId, Discount
import requests
import random

class MockAPIDiscountFetcher(DiscountFetcher):

    endpoint: str = "https://65f74b95b4f842e80885718b.mockapi.io/discounts"

    def __do_request(self, product_id: ProductId):

        """
        Do a request to the API.
        MockAPI cant handle nanoIDs or complex requests.
        So, for the sake of mockin data we try to fetch a 
        discount payload from a random INT ProductID.
        """

        # (Mock Data was constructed with IDs from 6 to 28)
        product_id = str(random.randint(6,28))

        return requests.get(f"{self.endpoint}/{product_id}")        

    async def fetch(self, product_id: ProductId) -> Discount | None:
        """ Concrete implementation to fetch a discount
        using a Webservice.
        """
        response = self.__do_request(product_id=product_id)
        
        if response.status_code == 200:
            payload = response.json()
            return Discount.of(payload['Value'])

        return None