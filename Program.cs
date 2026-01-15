var builder = WebApplication.CreateBuilder(args);

// Add Razor Pages support
builder.Services.AddRazorPages();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
}

app.UseStaticFiles();
app.UseRouting();

// Map Razor Pages
app.MapRazorPages();

app.Run();
