package com.example.BotMiddleware.Feign;


import com.example.BotMiddleware.DTO.CompaniesDTO;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;

@FeignClient(
        name = "TMDBFeignClient",
        url = "https://api.themoviedb.org/3"
)
public interface TMDBClient {

    @GetMapping("/search/company")
    CompaniesDTO[] getCompanies();
}
