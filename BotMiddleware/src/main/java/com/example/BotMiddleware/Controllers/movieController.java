package com.example.BotMiddleware.Controllers;


import com.example.BotMiddleware.Services.MovieService;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@EnableFeignClients
public class movieController {
    private final MovieService service;

    public movieController(MovieService service) {
        this.service = service;
    }

    @GetMapping("/search/companies")
    public int searchCompanies(@RequestParam() String keyword) {


        return 5;
    }
}
